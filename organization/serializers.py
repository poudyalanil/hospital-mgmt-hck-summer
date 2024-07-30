from rest_framework import serializers
from .models import Company

from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        serializer = UserSerializer(self.user).data
        for k, v in serializer.items():
            data[k] = v
        return data

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = [
                'id',
                'name',
                'description', 
                'city', 
                'address', 
                'phone', 'email', 'website',"logo"]
