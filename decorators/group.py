from django.contrib.auth.decorators import user_passes_test
from django.conf import settings


def group_required(*group_names, redirect_url=None):
    """
    Requires user membership in at least one of the groups passed in.
    The way to use this decorator is:
        @group_required(‘admins’, ‘seller’)
        def my_view(request, pk)
        ...
    """
    """
    To support modern django rest framework APIViews (class-based views).
    @method_decorator(group_required('groupa', 'groupb'))
    """

    if not redirect_url:
        redirect_url = settings.LOGIN_REDIRECT_URL

    def in_groups(user):
        if user.is_authenticated:
            if bool(user.groups.filter(name__in=group_names)) | user.is_superuser:
                return True
        return False

    actual_decorator = user_passes_test(
        in_groups,
        login_url=redirect_url
    )

    return actual_decorator
