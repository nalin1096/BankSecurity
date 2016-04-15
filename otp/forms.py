from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from material import *
from .models import BankUser

class UserForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('first_name','last_name','email','username', 'password1','password2')


class UserProfileForm(forms.ModelForm):
	class Meta:
		model = BankUser
		exclude = ('user','first_digit','second_digit','third_digit','fourth_digit','fifth_digit','sixth_digit','account_number','ifsc_code','amount')
	functions = (
		('',''),
		('a','a'),
		('b','b'),
		('c','c'),
		('d','d'),
		('e','e'),
		('f','f'),
		('g','d1'),
		('h','d2'),
		('i','m1'),
		('j','m2'),
		('k','min1'),
		('l','min2'),
	)
	modifier = (
		(' ',' '),
		('-','-'),
		('~','~'),
		('^2','^2'),
	)
	operator = (
		('',''),
		('+','+'),
		('*','*'),
	)

	a1 = forms.ChoiceField(choices=functions, required=False, label = "Operand 1")
	a2 = forms.ChoiceField(choices=modifier, required=False, label = "Modifier")
	a3 = forms.ChoiceField(choices=operator, required=False, label = "Operator")
	a4 = forms.ChoiceField(choices=functions, required=False, label = "Operand 2")
	a5 = forms.ChoiceField(choices=modifier, required=False, label = "Modifier")

	b1 = forms.ChoiceField(choices=functions, required=False, label = "Operand 1")
	b2 = forms.ChoiceField(choices=modifier, required=False, label = "Modifier")
	b3 = forms.ChoiceField(choices=operator, required=False, label = "Operator")
	b4 = forms.ChoiceField(choices=functions, required=False, label = "Operand 2")
	b5 = forms.ChoiceField(choices=modifier, required=False, label = "Modifier")

	c1 = forms.ChoiceField(choices=functions, required=False, label = "Operand 1")
	c2 = forms.ChoiceField(choices=modifier, required=False, label = "Modifier")
	c3 = forms.ChoiceField(choices=operator, required=False, label = "Operator")
	c4 = forms.ChoiceField(choices=functions, required=False, label = "Operand 2")
	c5 = forms.ChoiceField(choices=modifier, required=False, label = "Modifier")

	d1 = forms.ChoiceField(choices=functions, required=False, label = "Operand 1")
	d2 = forms.ChoiceField(choices=modifier, required=False, label = "Modifier")
	d3 = forms.ChoiceField(choices=operator, required=False, label = "Operator")
	d4 = forms.ChoiceField(choices=functions, required=False, label = "Operand 2")
	d5 = forms.ChoiceField(choices=modifier, required=False, label = "Modifier")

	e1 = forms.ChoiceField(choices=functions, required=False, label = "Operand 1")
	e2 = forms.ChoiceField(choices=modifier, required=False, label = "Modifier")
	e3 = forms.ChoiceField(choices=operator, required=False, label = "Operator")
	e4 = forms.ChoiceField(choices=functions, required=False, label = "Operand 2")
	e5 = forms.ChoiceField(choices=modifier, required=False, label = "Modifier")

	f1 = forms.ChoiceField(choices=functions, required=False, label = "Operand 1")
	f2 = forms.ChoiceField(choices=modifier, required=False, label = "Modifier")
	f3 = forms.ChoiceField(choices=operator, required=False, label = "Operator")
	f4 = forms.ChoiceField(choices=functions, required=False, label = "Operand 2")
	f5 = forms.ChoiceField(choices=modifier, required=False, label = "Modifier")


	def save (self, commit=True):
		a1 = self.cleaned_data.get('a1', None)
		a2 = self.cleaned_data.get('a2', None)
		a3 = self.cleaned_data.get('a3', None)
		a4 = self.cleaned_data.get('a4', None)
		a5 = self.cleaned_data.get('a5', None)

		b1 = self.cleaned_data.get('b1', None)
		b2 = self.cleaned_data.get('b2', None)
		b3 = self.cleaned_data.get('b3', None)
		b4 = self.cleaned_data.get('b4', None)
		b5 = self.cleaned_data.get('b5', None)

		c1 = self.cleaned_data.get('c1', None)
		c2 = self.cleaned_data.get('c2', None)
		c3 = self.cleaned_data.get('c3', None)
		c4 = self.cleaned_data.get('c4', None)
		c5 = self.cleaned_data.get('c5', None)

		d1 = self.cleaned_data.get('d1', None)
		d2 = self.cleaned_data.get('d2', None)
		d3 = self.cleaned_data.get('d3', None)
		d4 = self.cleaned_data.get('d4', None)
		d5 = self.cleaned_data.get('d5', None)

		e1 = self.cleaned_data.get('e1', None)
		e2 = self.cleaned_data.get('e2', None)
		e3 = self.cleaned_data.get('e3', None)
		e4 = self.cleaned_data.get('e4', None)
		e5 = self.cleaned_data.get('e5', None)

		f1 = self.cleaned_data.get('f1', None)
		f2 = self.cleaned_data.get('f2', None)
		f3 = self.cleaned_data.get('f3', None)
		f4 = self.cleaned_data.get('f4', None)
		f5 = self.cleaned_data.get('f5', None)


		return super(UserProfileForm, self).save(commit=commit)





