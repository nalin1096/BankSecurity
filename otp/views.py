from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserForm,UserProfileForm
from .models import BankUser
from django.contrib.auth.models import User
import random, re

# Create your views here.

def index (request):
	return render (request,'index.html')

def register(request):
	registered = False
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
			profile.save()
			registered = True
		else: 
			print user_form.errors, profile_form.errors
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()

	return render(request,'register.html',
		{'user_form': user_form, 'profile_form': profile_form,'registered': registered})


def user_login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		otp_code = request.POST['user_otp']
		test_user = authenticate(username=username, password=password)

		temp = request.session.get('random_number',None)
		digits = []			#digits in reverse order!
		while temp:
			digits.append(temp%10)
			temp = temp/10
		digits = digits[::-1]

		bank_user = BankUser.objects.get(user = test_user)

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

		if test_user and expected_otp==otp_code:
			if test_user.is_active:
				login(request, test_user)
				return HttpResponseRedirect('/')
			else:
				return HttpResponse("Your Bank account is disabled.")
		else:
			print "Invalid login details: {0}, {1}".format(username, password)
			return HttpResponse("Invalid login details supplied.")
	else:
		random_number = random.randint(100001,999999)
		request.session['random_number'] = random_number

		return render(request,'login.html',{'random_number':random_number})


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

	modifier = operand[1:operand_size:]

	if modifier == '':
		num = num
	elif modifier == '-':
		num = (10-num) % 10
	elif modifier == '~':
		num = (9-num)
	elif modifier == '^2':
		num = (num*num)%10
	elif modifier == '-^2':
		num = (10-num) % 10
		num = (num*num)%10
	elif modifier == '~^2':
		num = (9-num)
		num = (num*num)%10

	return num

@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/')






