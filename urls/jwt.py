from django.conf.urls import url
from CustomAuth.views import new_jwt_token

urlpatterns = [
    url('jwt/new', new_jwt_token, name='jwt revoke')
]
