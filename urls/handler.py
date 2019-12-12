from django.urls import path
from CustomAuth.views import page_not_found, permission_denied, server_error, unauthorized, bad_request

handler400 = bad_request
handler401 = unauthorized
handler403 = permission_denied
handler404 = page_not_found
handler500 = server_error
