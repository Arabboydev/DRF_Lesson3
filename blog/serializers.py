from .models import Category, EmployeeAbout
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class EmployeeAboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeAbout
        fields = "__all__"

    def validate_name(self, data):
        if data.isalpha():
            return data
        raise serializers.ValidationError({'name': 'Name connot consist of number only'})

    def validate_surname(self, data):
        if data.isalpha():
            return data
        raise serializers.ValidationError({'surname': 'Surname connot consist of number only'})

    def validate_phone(self, phone):
        number = phone.replace(' ', '')
        if number.isnumeric():
            return number.strip()
        raise serializers.ValidationError('Telefon raqam xato kiritildi!')


class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeAbout
        fields = "__all__"


