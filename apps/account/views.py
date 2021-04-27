from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import RegisterSerializer


User = get_user_model()

class RegistrationView(APIView):

    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response('Successfully registered', status=201)


class ActivationView(APIView):

    def post(self, request):
        phone = request.data.get('phone_number')
        code = request.data.get('activation_code')
        user = User.objects.filter(phone_number=phone, activation_code=code).first()
        if user is None:
            return Response('No such user', status=400)
        user.activation_code = ''
        user.is_active = True
        user.save()
        return Response('Successfully activated', status=200)