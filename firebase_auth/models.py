from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin



class UserAccountManager(BaseUserManager):
    def create_user(self, uid, email, first_name, last_name, password=None):
        if not email:
            raise ValueError('Email must be set!')
        if not uid:
            raise ValueError('UID error')
        user = self.model(uid=uid, email=email, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,uid, email, first_name, last_name, password):
        user = self.create_user(uid, email, first_name, last_name, password)
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, email_):
        return self.get(email=email_)


class UserAccount(AbstractBaseUser, PermissionsMixin):
    uid = models.CharField(max_length=200, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True) # default=False when you are going to implement Activation Mail
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['uid','first_name', 'last_name']

    def get_short_name(self):
        return self.email

    def get_full_name(self):
        return  self.email

    def has_perms(self, perm, ob=None):
        return True