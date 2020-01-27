from django.conf.urls import url
from CustomAuth.views import login

urlpatterns = [
    url(r'(?P<magic_uid64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', login, name='magic login'),
]
