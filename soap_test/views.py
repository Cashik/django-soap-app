from django.shortcuts import render

# the class with actual web methods
from soaplib.core.model.primitive import String
from soaplib.core.service import DefinitionBase, rpc
from soap_test.DjangoSoapAppModule import DjangoSoapApp


class MySOAPService(DefinitionBase):
    @rpc(String, String, _returns=String)
    def concat(self, f1, f2):
        return str(f1).upper()+str(f2).lower()

# Create your views here.

my_soap_service = DjangoSoapApp([MySOAPService], __name__)