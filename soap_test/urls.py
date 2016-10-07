from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'my_soap_service/service.wsdl', views.my_soap_service, name='my_soap_service'),
    url(r'my_soap_service/', views.my_soap_service, name='my_soap_service'),
]