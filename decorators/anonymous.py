from django.contrib.auth.decorators import user_passes_test
from django.conf import settings


def anonymous_required(function=None, redirect_url=None):
    """
    The way to use this decorator is:
        @anonymous_required
        def my_view(request, pk)
        ...
    """

    if not redirect_url:
        redirect_url = settings.LOGIN_REDIRECT_URL

    actual_decorator = user_passes_test(
        lambda u: u.is_anonymous(),
        login_url=redirect_url
    )

    if function:
        return actual_decorator(function)
    return actual_decorator
