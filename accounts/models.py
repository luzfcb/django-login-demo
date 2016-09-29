import re
from django.db import models
from django.core import validators
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager

class User(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(
        'usuário',
        max_length=30, unique=True, validators=[
            validators.RegexValidator(
                re.compile('^[\w.@+-]+$'),
                'Informe um usuário válido. Este valor deve conter apenas letras, números e os caracteres: @/./+/-/_ .',
                'invalid'
            )
        ]
    )
    name       = models.CharField(max_length=100, blank=True)
    email      = models.EmailField(unique=True, db_index=True)
    joined     = models.DateTimeField(auto_now_add=True)
    is_active  = models.BooleanField(default=True)
    is_staff   = models.BooleanField(default=False)
    birth_date = models.DateField(null=True, blank=True)
    avatar     = models.ImageField(upload_to='avatars/', null=True, blank=True)

    USERNAME_FIELD  = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    class Meta:
        db_table            = "users"
        verbose_name        = "Usuário"
        verbose_name_plural = "Usuários"

    def __str__(self):
        return self.name or self.username

    def get_full_name(self):
        return str(self)

    def get_short_name(self):
        return str(self).split(" ")[0]