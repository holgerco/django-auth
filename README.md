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
Add to `settings.py`
##### profile url

```python
USER_PROFILE_URL = '<your user profile url>' # default '/profile/'
```

##### login redirect url
```python
LOGIN_REDIRECT_URL = '<your login redirect>' # default '/account/profile/'
```

 
##### logout redirect url
```python
LOGOUT_REDIRECT = '<your logout redirect>' # default '/'
```
##### signup successfully redirect
```python
SIGNUP_SUCCESSFULLY_URL = '<your signup successfully redirect url>' # default '/profile/'
```

##### verification successfully redirect
```python
VERIFY_SUCCESSFULLY =  '<your verify successfully redirect url>' # default '/profile/' 
```

#### verification failed redirect
```python
VERIFY_FAILED = '<your verify failed redirect url>' # default 'Verification link is invalid!'
```
##### Email config
For verify email you should config email smtp server, example(gmail): 
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

### Magic Link
Use magic link for auto authentication user.
Add to `settings.py`
 ```python
AUTHENTICATION_BACKENDS = (
    # ... 
    'CustomAuth.backends.MagicLinkBackend', # magic backend
    # ...
)

MIDDLEWARE = [
    # ...
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # ...
    'CustomAuth.middleware.magic.MagicMiddleware', # Magic middleware
    # ...
]
```

### JWT Authentication
For get new jwt token with 2 month expire time.
    
    curl -H "jwt-authentication:<your token>" -X GET <your host>/jwt/token

For authenticate with jwt use your token.
    
    curl -H "jwt-authentication:<your token>" -X GET <your host>/<relative path>

### Multi database handling
For save user in multiple databases:
```python
AUTH_DATABASES = ['first database name', 'second database name', ... ]
```

## Versioning
This project follows [Semantic Versioning 2.0.0.](http://semver.org/spec/v2.0.0.html)

    
## License
This project follows the BSD license. See the [LICENSE](./LICENSE) for details.

* MIT: http://opensource.org/licenses/MIT