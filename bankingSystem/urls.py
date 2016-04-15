from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^transfer/$',views.transfer,name='transfer'),
	url(r'^home/$',views.home,name='home'),
	url(r'^summary/$',views.summary,name="summary"),
	url(r'^transfer_confirm/$',views.transfer_confirm,name="transfer_confirm"),
	url(r'^transaction_success/$',views.transaction_success,name='transaction_success'),
]
