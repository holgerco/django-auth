# Django custom user model

A Custom User model for authentication

## Requirement
* Python (3.5, 3.6, 3.7, 3.8)
* Django (1.11, >2.0, 2.1, 2.2, 3.0, 3.1)

## Installation
Install using ``pip``
    
    pip install django-custom-user-models
    
add to ``INSTALLED_APPS`` setting

    INSTALLED_APPS = {
        ...
        'CustomAuth',
        ...
    }

set ``AUTH_USER_MODEL`` setting
    
    AUTH_USER_MODEL = 'CustomUser.User'
   

## License
Uses the MIT license.

* MIT: http://opensource.org/licenses/MIT