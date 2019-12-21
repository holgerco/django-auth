from django.conf.urls import url
from CustomAuth.views import jwt_revoke

urlpatterns = [
    url('jwt/revoke', jwt_revoke, name='jwt revoke')
]
