from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.


class MyAccountManager(BaseUserManager):
    def create_user(self, username, phone_number, email, password=None):
        if not email:
             raise ValueError("User must have a email")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            phone_number=phone_number
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, phone_number, password=None, **extra_fields):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            phone_number=phone_number,
            password=password,
            **extra_fields,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superadmin = True
        user.save(using=self.db)
        return user

class Account(AbstractBaseUser):

    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    class Meta:
        ordering = ['email']

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phone_number']

    objects = MyAccountManager()



    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True
