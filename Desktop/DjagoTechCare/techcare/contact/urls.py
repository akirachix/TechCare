from django.conf.urls import url
from django.urls import path
from .views import contacts

app_name='contact'

urlpatterns=[
    url('contact/',contacts,name='contact'),
]