from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from .models import Computers,Phones
from .serializer import ComputersSerializer,PhonesSerializer

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod

    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getNotes(request):
	return "i'm protected"



def index(req):
    return JsonResponse('HELLO ELY FROM VIEWS', safe=False)

def myComputers(req):
    all_products = ComputersSerializer(Computers.objects.all(), many=True).data
    return JsonResponse(all_products, safe=False)

def myPhones(req):
    all_products = PhonesSerializer(Phones.objects.all(), many=True).data
    return JsonResponse(all_products, safe=False)

def allMyProducts(req):
    all_computers = ComputersSerializer(Computers.objects.all(), many=True).data
    all_phones = PhonesSerializer(Phones.objects.all(), many=True).data
    return JsonResponse(all_computers+all_phones, safe=False)





# def dollar_sign(req):
#     return ' $'