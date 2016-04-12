from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserForm,UserProfileForm
from .models import BankUser
from django.contrib.auth.models import User
import random, re
import datetime
from django.core.mail import EmailMessage

# Create your views here.

def index (request):
	return render (request,'index.html')

def about(request):
	return render (request,'about.html')

def forgot_password(request):
	valid = False
	if request.method == 'POST':
		email = request.POST['email']
		if len(User.objects.filter(email=email)) != 0:
			valid=True
			message = 'Please click on the following link to reset your password' + '\n\n' + 'http://192.168.55.22:8000/reset_password'+'\n\nSent from\nPseudo-Online Bank'
			email = EmailMessage('[Pseudo-Online Bank] Reset Password Link',message,to=[email])
			email.send()
		else:
			return HttpResponse("Invalid email id.")

	return render (request,'forgot_password.html',{'valid':valid})

def reset_password(request):
	correct_password = True
	if request.method == 'POST':
		username = request.POST['username']
		password1 = request.POST['new_password1']
		password2 = request.POST['new_password2']
		if password1==password2:
			correct_password=True
			temp = User.objects.get(username=username)
			temp.set_password(password1)
			temp.save()
			return HttpResponseRedirect("/")
		else:
			correct_password = False
	return render(request,'reset_password.html',{'correct_password':correct_password})

@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/')

def register(request):
	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)
		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			profile = profile_form.save(commit=False)
			profile.user = user
			data = profile_form.cleaned_data
			profile.first_digit = data.get('a1') + data.get('a2') + data.get('a3') + data.get('a4') + data.get('a5')
			profile.second_digit = data.get('b1') + data.get('b2') + data.get('b3') + data.get('b4') + data.get('b5')
			profile.third_digit = data.get('c1') + data.get('c2') + data.get('c3') + data.get('c4') + data.get('c5')
			profile.fourth_digit = data.get('d1') + data.get('d2') + data.get('d3') + data.get('d4') + data.get('d5')
			profile.fifth_digit = data.get('e1') + data.get('e2') + data.get('e3') + data.get('e4') + data.get('e5')
			profile.sixth_digit = data.get('f1') + data.get('f2') + data.get('f3') + data.get('f4') + data.get('f5')
			profile.address = data.get('address')
			profile.phone_number = data.get('phone_number')
			profile.dob = data.get('dob')
			if user.id==2:
				profile.account_number=str(1000000000000001)
			else:
				temp = User.objects.get(pk=user.id-1)
				temp_account = BankUser.objects.get(user=temp)
				temp_account_number = int(temp_account.account_number)
				profile.account_number=str(temp_account_number+1)

			profile.amount = 1000

			random_number = random.randint(0,9)
			profile.ifsc_code = get_ifsc(random_number)
			profile.save()
			request.session['reg_user'] = user.id
			return HttpResponseRedirect('/examples/')
		else: 
			print user_form.errors, profile_form.errors
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()

	return render(request,'register.html',
		{'user_form': user_form, 'profile_form': profile_form})


def otp_examples (request):
	registered = False
	if request.method == 'POST':
		example1 = request.POST['example1']
		example2 = request.POST['example2']

		test_user = User.objects.get(pk=request.session.get('reg_user',None))
		bank_user = BankUser.objects.get(user = test_user)

		temp1 = request.session.get('random_number1',None)
		temp2 = request.session.get('random_number2',None)

		expected_otp1 = get_otp(request.session.get('reg_user'),temp1)
		expected_otp2 = get_otp(request.session.get('reg_user'),temp2)

		if test_user and example1==expected_otp1 and example2==expected_otp2:
			if test_user.is_active:
				registered = True
				message = 'Congratulations!'+'\n\n'+'Your new account has been created. Your account details are as follows:\n\n\tUsername: '+test_user.username+'\n\tAccount Number: '+bank_user.account_number+'\n\tIFSC Code: '+bank_user.ifsc_code+'\n\tOTP Functions: \n\t\tFirst Digit: '+bank_user.first_digit+'\n\t\tSecond Digit: '+bank_user.second_digit+'\n\t\tThird Digit: '+bank_user.third_digit+'\n\t\tFourth Digit: '+bank_user.fourth_digit+'\n\t\tFifth Digit: '+bank_user.fifth_digit+'\n\t\tSixth Digit: '+bank_user.sixth_digit+'\n\nSent from\nPseudo-Online Bank'
				email = EmailMessage('[Pseudo-Online Bank] New Account Created',message,to=[test_user.email])
				email.send()
			else:
				return HttpResponse("Your Bank account is disabled.")
		else:
			return HttpResponse("Invalid login details supplied.")

	test_user = User.objects.get(pk=request.session.get('reg_user',None))
	bank_user = BankUser.objects.get(user = test_user)
	first_digit = bank_user.first_digit;
	second_digit = bank_user.second_digit;
	third_digit = bank_user.third_digit;
	fourth_digit = bank_user.fourth_digit;
	fifth_digit = bank_user.fifth_digit;
	sixth_digit = bank_user.sixth_digit;
	random_number1 = random.randint(100001,999999)
	random_number2 = random.randint(100001,999999)
	request.session['random_number1'] = random_number1
	request.session['random_number2'] = random_number2
	return render(request,'examples.html',
			{'registered':registered,'random_number1':random_number1,'random_number2':random_number2,
			'first_digit' : first_digit, 'second_digit':second_digit, 'third_digit':third_digit,
			'fourth_digit':fourth_digit, 'fifth_digit':fifth_digit, 'sixth_digit':sixth_digit})

def user_login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		# otp_code = request.POST['user_otp']
		test_user = authenticate(username=username, password=password)

		# temp = request.session.get('random_number',None)
		# expected_otp = get_otp(test_user.id,temp)
		
		if test_user:						#and expected_otp==otp_code
			if test_user.is_active:
				login(request, test_user)
				return HttpResponseRedirect('/home/')
			else:
				return HttpResponse("Your Bank account is disabled.")
		else:
			print "Invalid login details: {0}, {1}".format(username, password)
			return HttpResponse("Invalid login details supplied.")
	else:
		# random_number = random.randint(100001,999999)
		# request.session['random_number'] = random_number

		return render(request,'login.html')				#,{'random_number':random_number}

def otp_help (request):
	return render(request,'otp_help.html')

#HELPER FUNCTIONS
def get_otp (user_id,num):
	test_user = User.objects.get(pk=user_id)
	bank_user = BankUser.objects.get(user = test_user)

	temp = num
	digits = []			#digits in reverse order!
	while temp:
		digits.append(temp%10)
		temp = temp/10
	digits = digits[::-1]

	func1 = bank_user.first_digit.replace(" ","")
	func2 = bank_user.second_digit.replace(" ","")
	func3 = bank_user.third_digit.replace(" ","")
	func4 = bank_user.fourth_digit.replace(" ","")
	func5 = bank_user.fifth_digit.replace(" ","")
	func6 = bank_user.sixth_digit.replace(" ","")

	otp1 = otp_extract (digits,func1,0)
	otp2 = otp_extract (digits,func2,1)
	otp3 = otp_extract (digits,func3,2)
	otp4 = otp_extract (digits,func4,3)
	otp5 = otp_extract (digits,func5,4)
	otp6 = otp_extract (digits,func6,5)

	expected_otp = str(otp1)+str(otp2)+str(otp3)+str(otp4)+str(otp5)+str(otp6)
	print expected_otp
	return expected_otp

def otp_extract (digits,func,index):
	if func=='':
		return digits[index]
	func_size = len(func)
	operand1 = ''
	operand2 = ''
	operator = ''
	flag = 0
	for i in range(0,func_size):
		if func[i] != '+' and func[i] != '*':
			operand1 = operand1 + func[i]
		else:
			flag = i
			break
	
	operator = func[flag]
	
	for i in range(flag+1,func_size):
		operand2 = operand2 + func[i]

	sub1 = sub_func(digits,operand1)
	sub2 = sub_func(digits,operand2)

	if operator=='+':
		return (sub1+sub2)%10
	elif operator=='*':
		return (sub1*sub2)%10 

def sub_func (digits,operand):
	operand_size = len(operand)
	digit = operand[0]
	num = 0
	if digit == 'a':
		num = digits[0]
	elif digit == 'b':
		num = digits[1]
	elif digit == 'c':
		num = digits[2]
	elif digit == 'd':
		num = digits[3]
	elif digit == 'e':
		num = digits[4]
	elif digit == 'f':
		num = digits[5]
	elif digit == 'g':
		num = datetime.datetime.now().day
		if len(str(num)) == 1:
			num = 0
		else:
			num = num/10
	elif digit == 'h':
		num = datetime.datetime.now().day
		if len(str(num)) != 1:
			num = num % 10
	elif digit == 'i':
		num = datetime.datetime.now().month
		if len(str(num)) == 1:
			num = 0
		else:
			num = num/10
	elif digit == 'j':
		num = datetime.datetime.now().month
		if len(str(num)) != 1:
			num = num % 10
	elif digit == 'k':
		num = min(digits)
	elif digit == 'l':
		temp_digits = set(digits)
		temp_digits.remove(min(temp_digits))
		num = min(temp_digits)

	modifier = operand[1:operand_size:]

	if modifier == '':
		num = num
	elif modifier == '-':
		num = (10-num) % 10
	elif modifier == '~':
		num = (9-num)
	elif modifier == '^2':
		num = (num*num)%10

	return num

def get_ifsc(num):
	ifsc_list = [
		'ABCD0000001',
		'ABCD0000002',
		'ABCD0000003',
		'XYZW0000001',
		'XYZW0000002',
		'XYZW0000003',
		'QWERTY00001',
		'QWERTY00002',
		'QWERTY00003',
		'IIITD000001'
	]

	return ifsc_list[num]





