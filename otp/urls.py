from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.index,name='index'),
	url(r'^login/$',views.user_login,name='login'),
	url(r'^about/$',views.about,name='about'),
	url(r'^register/$',views.register,name='register'),
	url(r'^logout/$',views.user_logout,name='logout'),
	url(r'^examples/$',views.otp_examples,name="otp_examples"),
	url(r'^otp_help/$',views.otp_help, name="otp_help"),
	url(r'^forgot_password/$',views.forgot_password,name="forgot_password"),
	url(r'^reset_password/$',views.reset_password,name="reset_password"),
]