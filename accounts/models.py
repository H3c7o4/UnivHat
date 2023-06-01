from django.contrib.auth.models import PermissionsMixin\
    , AbstractBaseUser, BaseUserManager
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The email is not given.")
        if not password:
            raise ValueError('Password is not provided')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if not extra_fields.get('is_staff'):
            raise ValueError('Superuser must have is_staff = True')

        if not extra_fields.get('is_superuser'):
            raise ValueError('Superuser must have is_superuser = True')
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    GENDER_CHOICES = (
        (1, 'male'),
        (2, 'female'),
        (3, 'other')
    )

    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    gender = models.SmallIntegerField(choices=GENDER_CHOICES, null=True, blank=True)
    date_of_birth = models.DateField(auto_now_add=True)
    score = models.PositiveIntegerField(default=0)
    field_spec = models.CharField(max_length=50, null=True, blank=True)
    studying_at = models.CharField(max_length=50, null=True, blank=True)
    phone_number = models.CharField(max_length=16, null=True, blank=True)
    profile_pic = models.ImageField(upload_to='profile_images', default='blankProfilePic.jpg')
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.email
