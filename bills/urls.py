from django.conf.urls import url
from . import views

app_name = 'bills'
urlpatterns = [
    url(r'^$',views.accounts, name='accounts'),
    url(r'login/', views.login, name='login'),
    url(r'^create_account/$', views.createAccount, name="create_account"),
    url(r'^accounts/(?P<account_id>[0-9]+)/bills/$', views.accountBills, name="account_bills"),
]
