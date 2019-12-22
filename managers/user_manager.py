from django.contrib.auth.base_user import BaseUserManager
from django.utils import timezone
from datetime import datetime
import jwt
from django.conf import settings


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The email must be set')

        email = self.normalize_email(email=email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)

        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Creates and saves a superuser with the given email and password.
        """

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_verify', True)
        extra_fields.setdefault('date_verify', datetime.now())

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

    def get_by_token(self, token: str, algorithm='HS256'):
        encoded_token = token.encode('utf-8')
        try:
            decoded: dict = jwt.decode(encoded_token, settings.SECRET_KEY, algorithm)
            user_id = decoded.get('id', None)
            if user_id:
                user = self.get(pk=user_id)
                return user
            user_email = decoded.get('email', None)
            if user_email:
                user = self.get(email=user_email)
                return user
            user_username = decoded.get('username', None)
            if user_username:
                user = self.get(username=user_username)
                return user
        except jwt.ExpiredSignatureError:
            return None  # Signature expired. Please log in again.
        except jwt.InvalidTokenError:
            return None  # Invalid token. Please log in again.
        except self.model.DoesNotExist:
            return None  # User does not exist
