from json import JSONEncoder
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from firebase_admin import auth
from django.contrib.auth import get_user_model
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from firebase_auth.serializer import UserSerializer
from rest_framework.permissions import IsAuthenticated
    
class RegisterUser(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            user = auth.create_user(
                    email=request.data['email'],
                    password=request.data['password']
                )
            if user.uid:
                User = get_user_model()
                user_obj = User.objects.create(
                    uid=user.uid,
                    email=request.data['email'],
                    first_name=request.data['firstName'],
                    last_name=request.data['lastName'],
                )
                user_obj.save()
                print(user_obj)
                return Response({"user":"success"}, status=HTTP_200_OK)
            else:
                return Response({ "email":"User could not be created",
                        "password": "",
                        "firstName": "",
                        "lastName": "",
                        }, status=HTTP_400_BAD_REQUEST)
        except Exception as e:
            error = str(e)
            print("ERROR AUTH", error)
            errors = { "email":"",
                        "password": "",
                        "firstName": "",
                        "lastName": "",
                        }

            if 'email' in error:
                errors['email'] = error
            if 'password' in error:
                errors['password'] = error
            if 'firstName' in error:
                errors['firstName'] = error
            if 'lastName' in error:
                errors['lastName'] = error
        
            return Response(errors, status=HTTP_400_BAD_REQUEST)

class UserInfo(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        User = get_user_model()
        user = User.objects.get(uid=request.user.uid)
        if user:
            return Response({
                "email": user.email,
                "firstName": user.first_name,
                "lastName": user.last_name,

            }, status=HTTP_200_OK)
        else:
            return Response({}, status=HTTP_400_BAD_REQUEST)