from django.core.exceptions import PermissionDenied


def verify_required(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_anonymous or not request.user.is_verify:
            return
        else:
            return function(request, *args, **kwargs)
