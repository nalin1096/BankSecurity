from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from otp.models import BankUser
from django.contrib.auth.decorators import login_required
from .models import Transaction
from django.core.mail import EmailMessage
from datetime import datetime
import random

# Create your views here.

@login_required
def home(request):
	test_user = User.objects.get(pk=request.user.id)
	bank_user = BankUser.objects.get(user = test_user)
	username = bank_user.user.username
	first_name = bank_user.user.first_name
	last_name = bank_user.user.last_name
	email = bank_user.user.email
	account_number = bank_user.account_number
	amount = bank_user.amount
	ifsc = bank_user.ifsc_code
	first_digit = bank_user.first_digit
	second_digit = bank_user.second_digit
	third_digit = bank_user.third_digit
	fourth_digit = bank_user.fourth_digit
	fifth_digit = bank_user.fifth_digit
	sixth_digit = bank_user.sixth_digit
	address = bank_user.address
	phone_number = bank_user.phone_number
	dob = bank_user.dob
	# sent_transaction_entries = Transaction.objects.filter(sender=account_number) 	
	# received_transaction_entries = Transaction.objects.filter(receiver=account_number) 	
	return render(request,'view_profile.html',
		{'username':username,'account_number':account_number,'amount':amount,'ifsc':ifsc, 'first_name':first_name,
		'last_name':last_name,'email':email,'first_digit':first_digit,'second_digit':second_digit,
		'third_digit':third_digit,'fourth_digit':fourth_digit,'fifth_digit':fifth_digit,'sixth_digit':sixth_digit,
		'address':address,'phone_number':phone_number,'dob':dob})

@login_required
def summary(request):
	test_user = User.objects.get(pk=request.user.id)
	bank_user = BankUser.objects.get(user = test_user)
	username = bank_user.user.username
	entry = Transaction.objects.filter(primary_account=bank_user.account_number)
	return render(request,'account_summary.html',{'entry':entry,'username':username})

@login_required
def transfer(request):
	user_exists = True
	ifsc_exists = True
	balance_exists = True
	test_user = User.objects.get(pk=request.user.id)
	bank_user = BankUser.objects.get(user = test_user)
	balance = bank_user.amount
	if request.method == 'POST':
		ifsc = str(request.POST['ifsc'])
		account = str(request.POST['account'])
		amount = int(request.POST['amount'])

		if len(BankUser.objects.filter(ifsc_code=ifsc)) == 0:
			ifsc_exists = False
			return render(request,'transaction.html',{'balance':balance,'user_exists':user_exists,'ifsc_exists':ifsc_exists,'balance_exists':balance_exists})

		if len(BankUser.objects.filter(ifsc_code=ifsc,account_number=account)) == 0:
			user_exists = False
			return render(request,'transaction.html',{'balance':balance,'user_exists':user_exists,'ifsc_exists':ifsc_exists,'balance_exists':balance_exists})

		sender = BankUser.objects.get(user = request.user)
		if sender.amount < amount:
			balance_exists = False
			return render(request,'transaction.html',{'balance':balance,'user_exists':user_exists,'ifsc_exists':ifsc_exists,'balance_exists':balance_exists})
		
		# sender.amount = sender.amount - amount
		# sender.save()
		# receiver = BankUser.objects.get(account_number=account)
		# receiver.amount = receiver.amount + amount
		# receiver.save()

		# transaction_entry = Transaction(primary_account=str(sender.account_number),secondary_account=account,amount=amount,transfer_type='Db',time=datetime.now(),balance_remaining=sender.amount)
		# transaction_entry.save()
		# transaction_entry = Transaction(primary_account=account,secondary_account=str(sender.account_number),amount=amount,transfer_type='Cr',time=datetime.now(),balance_remaining=receiver.amount)
		# transaction_entry.save()

		# messageToReciever = 'Congratulations!'+'\n\n'+'You have received Rs.'+ str(amount) +' from '+ str(sender.user.first_name) + ' '+  str(sender.user.last_name)+'.'+'\n\n'+'Sent from\nPseudo-Online Bank'
		# email = EmailMessage('[Pseudo-Online Bank] Money Received',messageToReciever,to=[receiver.user.email])
		# email.send()

		# messageToSender = 'Greetings!'+'\n\n'+'This is to confirm that you have just transferred Rs.'+ str(amount) + ' into the account of ' + str(receiver.user.first_name)+ ' ' + str(receiver.user.last_name) +'.'+'\n\n'+'Sent from\nPseudo-Online Bank' 
		# email = EmailMessage('[Pseudo-Online Bank] Money Transferred',messageToSender,to=[sender.user.email])
		# email.send()

		random_number = random.randint(100001,999999)
		request.session['random_number'] = random_number
		request.session['receiver_acc'] = account
		request.session['amount'] = amount

		message = 'Greetings!'+'\n\n'+'This is your randomly generated OTP: '+str(random_number)+'\n\n'+'Sent from\nPseudo-Online Bank'
		email = EmailMessage('[Pseudo-Online Bank] Confirmation OTP',message,to=[sender.user.email])
		email.send()

		return HttpResponseRedirect('/transfer_confirm/')
	return render(request,'transaction.html',{'balance':balance,'user_exists':user_exists,'ifsc_exists':ifsc_exists,'balance_exists':balance_exists})

@login_required
def transfer_confirm(request):
	flag = True
	test_user = User.objects.get(pk=request.user.id)
	bank_user = BankUser.objects.get(user = test_user)
	if request.method == 'POST':
		otp = request.POST['user_otp']

		temp = request.session.get('random_number',None)
		account = request.session.get('receiver_acc',None)
		amount = request.session.get('amount',None)
		expected_otp = get_otp(test_user.id,temp)

		if otp==expected_otp:
			sender = BankUser.objects.get(user = request.user)
			sender.amount = sender.amount - amount
			sender.save()
			receiver = BankUser.objects.get(account_number=account)
			receiver.amount = receiver.amount + amount
			receiver.save()

			transaction_entry = Transaction(primary_account=str(sender.account_number),secondary_account=account,amount=amount,transfer_type='Db',time=datetime.now(),balance_remaining=sender.amount)
			transaction_entry.save()
			transaction_entry = Transaction(primary_account=account,secondary_account=str(sender.account_number),amount=amount,transfer_type='Cr',time=datetime.now(),balance_remaining=receiver.amount)
			transaction_entry.save()

			messageToReciever = 'Congratulations!'+'\n\n'+'You have received Rs.'+ str(amount) +' from '+ str(sender.user.first_name) + ' '+  str(sender.user.last_name)+'.'+'\n\n'+'Sent from\nPseudo-Online Bank'
			email = EmailMessage('[Pseudo-Online Bank] Money Received',messageToReciever,to=[receiver.user.email])
			email.send()

			messageToSender = 'Greetings!'+'\n\n'+'This is to confirm that you have just transferred Rs.'+ str(amount) + ' into the account of ' + str(receiver.user.first_name)+ ' ' + str(receiver.user.last_name) +'.'+'\n\n'+'Sent from\nPseudo-Online Bank' 
			email = EmailMessage('[Pseudo-Online Bank] Money Transferred',messageToSender,to=[sender.user.email])
			email.send()

			return HttpResponseRedirect('/home/')
		else:
			flag = False
			return render (request,'transfer_confirm.html',{'flag':flag})
	return render (request,'transfer_confirm.html',{'flag':flag})



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





