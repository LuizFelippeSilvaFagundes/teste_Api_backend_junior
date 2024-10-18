from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email, nome, data_de_nascimento, password=None):
        if not email:
            raise ValueError('O usuário deve ter um email')
        user = self.model(
            email=self.normalize_email(email),
            nome=nome,
            data_de_nascimento=data_de_nascimento,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nome, data_de_nascimento, password=None):
        user = self.create_user(email, nome, data_de_nascimento, password)
        user.is_admin = True
        user.save(using=self._db)
        return user

class Usuario(AbstractBaseUser):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    data_de_nascimento = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome', 'data_de_nascimento']

    def __str__(self):
        return self.email
