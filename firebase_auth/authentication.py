import os

import firebase_admin
from firebase_admin import credentials
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone
from firebase_admin import auth
from firebase_admin import credentials
from rest_framework import authentication
from rest_framework import exceptions

from .exceptions import FirebaseError
from .exceptions import InvalidAuthToken
from .exceptions import NoAuthToken
import json
cred = credentials.Certificate(json.loads(os.environ['FIREBASE_JSON']))
# firebase_admin.initialize_app(cred)
app = firebase_admin.initialize_app(cred)

#  os.environ.get("FIREBASE_CLIENT_CERT_URL"),
# cred = credentials.Certificate(os.path.join(
#     os.path.dirname(__file__), 'secrets/firebaseconfig.json'))

# app = firebase_admin.initialize_app(cred)


class FirebaseAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.META.get("HTTP_AUTHORIZATION")
        if not auth_header:
            raise NoAuthToken("No auth token provided")

        id_token = auth_header.split(" ").pop()
        decoded_token = None
        try:
            decoded_token = auth.verify_id_token(id_token)
        except Exception as e:
            raise InvalidAuthToken("Invalid auth token")
            pass

        if not id_token or not decoded_token:
            return None

        try:
            uid = decoded_token.get("uid")
        except Exception:
            raise FirebaseError()
        User = get_user_model()

        user = User.objects.get(uid=uid)
        return (user, None)
