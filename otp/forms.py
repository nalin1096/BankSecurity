from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from material import *
from .models import BankUser

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    layout = Layout (
    	Fieldset (
    		'Personal Information',
    		Row ('first_name','last_name'),
    		'email'
    	),
    	'username',
    	'password'
    )

    class Meta:
        model = User
        fields = ('first_name','last_name','username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
	class Meta:
		model = BankUser
		exclude = ('user','first_digit','second_digit','third_digit','fourth_digit','fifth_digit','sixth_digit')
	functions = (
		('',''),
		('a','a'),
		('b','b'),
		('c','c'),
		('d','d'),
		('e','e'),
		('f','f'),
	)
	modifier = (
		(' ',' '),
		('-','-'),
		('~','~'),
		('^2','^2'),
		('-^2','-^2'),
		('~^2','~^2'),
	)
	operator = (
		('',''),
		('+','+'),
		('*','*'),
	)

	a1 = forms.ChoiceField(choices=functions, required=False)
	a2 = forms.ChoiceField(choices=modifier, required=False)
	a3 = forms.ChoiceField(choices=operator, required=False)
	a4 = forms.ChoiceField(choices=functions, required=False)
	a5 = forms.ChoiceField(choices=modifier, required=False)

	b1 = forms.ChoiceField(choices=functions, required=False)
	b2 = forms.ChoiceField(choices=modifier, required=False)
	b3 = forms.ChoiceField(choices=operator, required=False)
	b4 = forms.ChoiceField(choices=functions, required=False)
	b5 = forms.ChoiceField(choices=modifier, required=False)

	c1 = forms.ChoiceField(choices=functions, required=False)
	c2 = forms.ChoiceField(choices=modifier, required=False)
	c3 = forms.ChoiceField(choices=operator, required=False)
	c4 = forms.ChoiceField(choices=functions, required=False)
	c5 = forms.ChoiceField(choices=modifier, required=False)

	d1 = forms.ChoiceField(choices=functions, required=False)
	d2 = forms.ChoiceField(choices=modifier, required=False)
	d3 = forms.ChoiceField(choices=operator, required=False)
	d4 = forms.ChoiceField(choices=functions, required=False)
	d5 = forms.ChoiceField(choices=modifier, required=False)

	e1 = forms.ChoiceField(choices=functions, required=False)
	e2 = forms.ChoiceField(choices=modifier, required=False)
	e3 = forms.ChoiceField(choices=operator, required=False)
	e4 = forms.ChoiceField(choices=functions, required=False)
	e5 = forms.ChoiceField(choices=modifier, required=False)

	f1 = forms.ChoiceField(choices=functions, required=False)
	f2 = forms.ChoiceField(choices=modifier, required=False)
	f3 = forms.ChoiceField(choices=operator, required=False)
	f4 = forms.ChoiceField(choices=functions, required=False)
	f5 = forms.ChoiceField(choices=modifier, required=False)

	fieldsets = (
        ('first_digit', {
            'fields': ('a1', 'a2', 'a3','a4','a5',),
        }),
        ('second_digit', {
            'fields': ('b1', 'b2', 'b3','b4','b5',),
        }),
        ('third_digit', {
            'fields': ('c1', 'c2', 'c3','c4','c5',),
        }),
        ('fourth_digit', {
            'fields': ('d1', 'd2', 'd3','d4','d5',),
        }),
        ('fifth_digit', {
            'fields': ('e1', 'e2', 'e3','e4','e5',),
        }),
        ('sixth_digit', {
            'fields': ('f1', 'f2', 'f3','f4','f5',),
        }),
    )

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

	layout = Layout(
			Fieldset (
				'First Digit',
				Row('a1',
				'a2',
				'a3',
				'a4',
				'a5')
			),
			Fieldset (
				'Second Digit',
				Row('b1',
				'b2',
				'b3',
				'b4',
				'b5')
			),
			Fieldset (
				'Third Digit',
				Row('c1',
				'c2',
				'c3',
				'c4',
				'c5')
			),
			Fieldset (
				'Fourth Digit',
				Row('d1',
				'd2',
				'd3',
				'd4',
				'd5')
			),
			Fieldset (
				'Fifth Digit',
				Row('e1',
				'e2',
				'e3',
				'e4',
				'e5')
			),
			Fieldset (
				'Sixth Digit',
				Row('f1',
				'f2',
				'f3',
				'f4',
				'f5')
			),
		)



