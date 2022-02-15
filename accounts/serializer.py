from rest_framework import serializers
from.models import User,ServiceDetails,ClothDetails,PriceDetails,AccountDetails,PlantDetails
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['email','phone','address','image','username','password']
        

    def validate_password(self, value: str) -> str:
        # """
        # Hash value passed by user.

        # :param value: password of a user
        # :return: a hashed version of the password
        # """
        return make_password(value)

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model=ServiceDetails
        fields=['serviceName','serviceCode']


class ClothSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClothDetails
        fields = ['clothName','clothNameArabic','clothCode','clothImg']


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceDetails
        fields = ['serviceName','clothType','price','xprice']

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountDetails
        fields = ['acTypeName']

class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantDetails
        fields = ['plantName','location','clothType','contactName','ontactNumber'],
        