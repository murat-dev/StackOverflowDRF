from django.contrib.auth import get_user_model
from rest_framework import serializers

from apps.account.utils import send_activation_sms

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, write_only=True, required=True)
    password_confirmation = serializers.CharField(min_length=8, write_only=True, required=True)

    class Meta:
        model = User
        fields = ['phone_number', 'username', 'password', 'password_confirmation']

    def validate_phone_number(self, phone_number):
        if User.objects.filter(phone_number=phone_number).exists():
            raise serializers.ValidationError('Пользователь я данным номером существует!')
        return phone_number


    def validate_username(self, username):
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError('Пользователь я данным номером существует!')
        return username


    def validate(self, attrs):
        password = attrs.get('password')
        password_confirmation = attrs.pop('password_confirmation', None)
        if password != password_confirmation:
            raise serializers.ValidationError('Пароли не совпадают')

        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        send_activation_sms(user)
        return user
