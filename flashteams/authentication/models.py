from django.db import models
from django.contrib.auth.models import (AbstractUser, BaseUserManager)
from django.contrib.postgres.fields import JSONField
from django.core.serializers.json import DjangoJSONEncoder
from datetime import datetime, timedelta
import jwt
from utils.models import BaseAbstractModel
from utils.managers import CustomQuerySet


class UserManager(BaseUserManager):
    """
    We need to override the `create_user` method so that users can
    only be created when all non-nullable fields are populated.
    """

    def create_user(
        self,
        first_name=None,
        last_name=None,
        email=None,
        password=None,
        role='TL'
    ):
        """
        Create and return a `User` with an email, first name, last name and
        password.
        """
        if not first_name:
            raise TypeError('Users must have a first name.')

        if not last_name:
            raise TypeError('Users must have a last name.')

        if not email:
            raise TypeError('Users must have an email address.')

        if not password:
            raise TypeError('Users must have a password.')

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            email=self.normalize_email(email),
            username=self.normalize_email(email))
        user.set_password(password)
        user.role = role
        user.save()
        return user


class User(AbstractUser, BaseAbstractModel):
    """
    This class defines the User model
    """
    USER_ROLES = (
        ('TL', 'Team Lead'),
        ('TM', 'Team Member'),
    )

    username = models.CharField(null=True, blank=True, max_length=100, unique=True)
    card_info = JSONField(verbose_name='tokenized card details', encoder=DjangoJSONEncoder, default=dict)
    email = models.EmailField(unique=True)
    role = models.CharField(verbose_name='user role', max_length=2, choices=USER_ROLES, default='TM')
    is_verified = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()
    active_objects = CustomQuerySet.as_manager()

    def __str__(self):
        return f'{self.email}'

    

