from .handler import handler400, handler401, handler403, handler404, handler500
from django.conf.urls import url
from CustomAuth.views import login, verify_email, signup, logout, resend_verification_code

urlpatterns = [
    url('login/', login, name='login'),
    url('signup/', signup, name='signup'),
    url('logout/', logout, name='logout'),
    url('verify/resend/', resend_verification_code, name='resend verify'),
    url(r'^verify/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', verify_email,
        name='verify'),
]
