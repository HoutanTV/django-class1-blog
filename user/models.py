from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
# Create your models here.


class UserManager(BaseUserManager):

    def create_user(self, email, first_name, password=None, **extra_fields):

        if not email:
            raise ValueError('Email field is required')
        if not first_name:
            raise ValueError('First name is required.')
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, first_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('super user should has is_staff True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('super user should has is_superuser True')

        return self.create_user(email, first_name, password, **extra_fields)
        #is_staff
        #is_superuser


class User(AbstractUser):
    email = models.EmailField(unique=True)
    birthday = models.DateField(null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']

    objects = UserManager()

    class Meta:
        db_table = 'auth_user'

    def __str__(self):
        return self.username

class Profile(models.Model):
    GENDER_CHOICES = [
        ("M", "Male"),
        ("F", "Female")
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(upload_to='profile_images/')
    bio = models.TextField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
