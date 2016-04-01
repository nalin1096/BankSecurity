from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.index,name='index'),
	url(r'^login/$',views.user_login,name='login'),
	url(r'^register/$',views.register,name='register'),
	url(r'^logout/$',views.user_logout,name='logout'),
	url(r'^examples/$',views.otp_examples,name="otp_examples"),
	url(r'^otp_help/$',views.otp_help, name="otp_help"),
]