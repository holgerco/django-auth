from .handler import handler400, handler401, handler403, handler404, handler500
from django.conf.urls import url
from CustomAuth.views import login, verify_email, signup, logout, resend_verification_code

from .password import urlpatterns as password_patterns
from .jwt import urlpatterns as jwt_patterns
from .social import urlpatterns as social_patterns

urlpatterns = [
    url('login/', login, name='login'),
    url('signup/', signup, name='signup'),
    url('logout/', logout, name='logout'),
    url('verify/resend/', resend_verification_code, name='resend verify'),
    url(r'^verify/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', verify_email,
        name='verify'),
]

urlpatterns += password_patterns
urlpatterns += jwt_patterns
urlpatterns += social_patterns
