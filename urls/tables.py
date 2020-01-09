from django.urls import path
from CustomAuth.views import user_list, superuser_list, staff_list
from django.views.generic.base import RedirectView
urlpatterns = [
    path("user/list/", RedirectView.as_view(url="all")),
    path("user/list/all", user_list),
    path("user/list/superuser", superuser_list),
    path("user/list/staff", staff_list)
]
