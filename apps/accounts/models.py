from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin

# Create your models here.

class UserManager(BaseUserManager):


    def create_user(self, email, username, password = None, **extrafields):

        if not email:
            return ValueError("Email is required !")
        
        email = self.normalize_email(email)

        user = self.model(
            email=email,
            username= username,
            **extrafields
        )

        user.set_password(password)
        user.save(self._db)

        return user
    

    def create_superuser(self, email, username, password, **extrafields):

        extrafields.setdefault('is_staff',True)
        extrafields.setdefault('is_superuser', True)

        return self.create_user(email, username, password, **extrafields)


class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150,unique=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)


    data_joined = models.DateTimeField(auto_now_add=True)


    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )

    bio = models.CharField(max_length=500,blank=True)
    profile_pic = models.ImageField(upload_to='static/profile_pic',blank=True)
    create_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email}\'s Profile !"
    




