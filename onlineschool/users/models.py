import email
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

GENDER_CHOICES = (
    ("Erkak","Erkak"),
    ("Ayol","Ayol")
)

class CustomUser(AbstractUser):
    email = models.EmailField(_('email adress'))
    phone = models.CharField(_('phone number'), max_length=13, unique=True)
    gender = models.CharField(_('gender'), choices=GENDER_CHOICES, max_length=5)
    name = models.CharField(_('name'), max_length=20)
    lastname = models.CharField(_('lastname'), max_length=20)
    sinf = models.IntegerField(_('class'))

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['email', 'username', 'name', 'sinf']

    objects = CustomUserManager()

    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name + self.lastname

    class Meta:
        verbose_name = 'Foydalanuvchi'
        verbose_name_plural = 'Foydalanuvchilar'
