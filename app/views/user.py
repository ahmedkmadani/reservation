import datetime
import jwt
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models.user import User
from app.serializers.user import UserSerializers


class RegisterView(APIView):
    def post(request):
        serializer = UserSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginView(APIView):
    def post(self, request):
        employee_number = request.data['employee_number']
        password = request.data['password']

        user = User.objects.filter(employee_number=employee_number).first()

        if user is None:
            raise AuthenticationFailed('User not found')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30),
            'iat': datetime.datetime.utcnow(),
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        res = Response()
        res.set_cookie(key='jwt', value=token, httponly=True)
        res.data = {
            'jwt': token
        }

        return res


class UserLogoutView(APIView):
    def post(self, request):
        res = Response()
        res.delete_cookie('jwt')
        res.data = {
            'msg': 'success'
        }
        return res
