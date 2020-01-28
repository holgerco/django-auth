from django.contrib.auth.base_user import BaseUserManager
from django.utils import timezone
from datetime import datetime
import jwt
from django.conf import settings

class UserManager(BaseUserManager):
    def create_user(self, cellphone, password=None, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not cellphone:
            raise ValueError('The cellphone must be set')

        cellphone = self.normalize_email(email=cellphone)
        user = self.model(cellphone=cellphone, **extra_fields)
        user.set_password(password)
        databases = getattr(settings, 'AUTH_DATABASES', [])
        if databases:
            for db in databases:
                user.save(using=db)
        else:
            user.save(using=self.db)

        return user

    def create_superuser(self, cellphone, password, **extra_fields):
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

        return self.create_user(cellphone, password, **extra_fields)

    def get_by_token(self, token: str, algorithm='HS256'):
        """
        :param token: Equivalent to a user's token information. Based on the token, the user is identified
        :param algorithm: The algorithm used for encoding the token
        :return: If the token is valid, returns a specific user in the other way return null
        """
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
            user_cellphone = decoded.get('cellphone', None)
            if user_cellphone:
                user = self.get(cellphone=user_cellphone)
                return user

        except jwt.ExpiredSignatureError:
            return None  # Signature expired. Please log in again.
        except jwt.InvalidTokenError:
            return None  # Invalid token. Please log in again.
        except self.model.DoesNotExist:
            return None  # User does not exist


class SuperuserManager(BaseUserManager):
    def get_queryset(self):
        return super().get_queryset().filter(is_superuser=True)

    def create(self, cellphone, password, **extra_fields):
        return self.create_user(cellphone, password, **extra_fields)

    def create_user(self, cellphone, password, **extra_fields):
        """
        Creates and saves a superuser with the given email and password.
        """

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_verify', True)
        extra_fields.setdefault('date_verify', timezone.now())

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        if not cellphone:
            raise ValueError('The cellphone must be set')

        user = self.model(cellphone=cellphone, **extra_fields)
        user.set_password(password)
        databases = getattr(settings, 'AUTH_DATABASES', [])
        if databases:
            for db in databases:
                user.save(using=db)
        else:
            user.save(using=self.db)

        return user

    def get_by_token(self, token: str, algorithm='HS256'):
        """
        :param token: Equivalent to a user's token information. Based on the token, the user is identified
        :param algorithm: The algorithm used for encoding the token
        :return: If the token is valid, returns a specific user in the other way return null
        """
        encoded_token = token.encode('utf-8')
        try:
            decoded: dict = jwt.decode(encoded_token, settings.SECRET_KEY, algorithm)
            user_id = decoded.get('id', None)
            if user_id:
                user = self.get(pk=user_id, is_superuser=True)
                return user
            user_email = decoded.get('email', None)
            if user_email:
                user = self.get(email=user_email, is_superuser=True)
                return user
            user_username = decoded.get('username', None)
            if user_username:
                user = self.get(username=user_username, is_superuser=True)
                return user
            user_cellphone = decoded.get('cellphone', None)
            if user_cellphone:
                user = self.get(cellphone=user_cellphone, is_superuser=True)
                return user
        except jwt.ExpiredSignatureError:
            return None  # Signature expired. Please log in again.
        except jwt.InvalidTokenError:
            return None  # Invalid token. Please log in again.
        except self.model.DoesNotExist:
            return None  # User does not exist


class StaffManager(BaseUserManager):
    def get_queryset(self):
        return super().get_queryset().filter(is_staff=True)

    def create(self, cellphone, password, **extra_fields):
        return self.create_user(cellphone, password, **extra_fields)

    def create_user(self, cellphone, password, **extra_fields):
        """
        Creates and saves a superuser with the given cellphone and password.
        """

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_verify', True)
        extra_fields.setdefault('date_verify', timezone.now())

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')

        if not cellphone:
            raise ValueError('The cellphone must be set')

        user = self.model(cellphone=cellphone, **extra_fields)
        user.set_password(password)
        databases = getattr(settings, 'AUTH_DATABASES', [])
        if databases:
            for db in databases:
                user.save(using=db)
        else:
            user.save(using=self.db)

        return user

    def get_by_token(self, token: str, algorithm='HS256'):
        """
        :param token: Equivalent to a user's token information. Based on the token, the user is identified
        :param algorithm: The algorithm used for encoding the token
        :return: If the token is valid, returns a specific user in the other way return null
        """
        encoded_token = token.encode('utf-8')
        try:
            decoded: dict = jwt.decode(encoded_token, settings.SECRET_KEY, algorithm)
            user_id = decoded.get('id', None)
            if user_id:
                user = self.get(pk=user_id, is_staff=True)
                return user
            user_email = decoded.get('email', None)
            if user_email:
                user = self.get(email=user_email, is_staff=True)
                return user
            user_username = decoded.get('username', None)
            if user_username:
                user = self.get(username=user_username, is_staff=True)
                return user
            user_cellphone = decoded.get('cellphone', None)
            if user_cellphone:
                user = self.get(cellphone=user_cellphone, is_staff=True)
                return user
        except jwt.ExpiredSignatureError:
            return None  # Signature expired. Please log in again.
        except jwt.InvalidTokenError:
            return None  # Invalid token. Please log in again.
        except self.model.DoesNotExist:
            return None  # User does not exist
