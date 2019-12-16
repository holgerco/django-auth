# Django custom user model

A Custom User model for authentication

## Requirement
* Python (3.5, 3.6, 3.7, 3.8)
* Django (1.11, >2.0, 2.1, 2.2, 3.0, 3.1)

## Installation
Install using ``pip``
    
    pip install django-custom-user-models
    
Add to ``INSTALLED_APPS`` setting

    INSTALLED_APPS = {
        ...
        'CustomAuth',
        ...
    }

Set ``AUTH_USER_MODEL`` setting before first migrate
    
    AUTH_USER_MODEL = 'CustomAuth.User'
    
Migrate apps

    py manage.py migrate
    
## Usage

### Status Handler
Add ``handler`` to ``yourproject/urls.py``
```python
from CustomAuth.urls import handler400, handler401, handler403, handler404, handler500
```

### Authentication template
##### profile url
Add to `settings.py`
```python
USER_PROFILE_URL = 'your user profile url' # default '/profile/'
```
 
##### logout redirect url
Add to `settings.py`
```python
LOGOUT_REDIRECT = 'your logout redirect' # default '/'
```
##### signup successfully redirect
Add to `settings.py`
```python
SIGNUP_SUCCESSFULLY_URL = 'your signup successfully redirect url' # default '/profile/'
```

##### verification successfully redirect
Add to `settings.py`
```python
VERIFY_SUCCESSFULLY =  'your verify successfully redirect url' # default '/profile/' 
```

#### verification failed redirect
Add to `settings.py`
```python
Verify_Failed = 'your verify failed redirect url' # default 'Verification link is invalid!'
```
##### Gmail config
For verify email you must config email smtp server 
```python
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'your name@gmail.com'
EMAIL_HOST_PASSWORD = 'your password'
EMAIL_USE_TSL = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
EMAIL_FROM = EMAIL_HOST_USER
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
```


    
## License
Uses the MIT license.

* MIT: http://opensource.org/licenses/MIT