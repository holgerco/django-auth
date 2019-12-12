from django.shortcuts import render


def page_not_found(request, exception=None):
    context = {
        'title': 'Page not found',
        'text': 'Sorry page not found',
        'code': 404
    }
    return render(request, 'CustomAuth/pages/status.html', context=context)


def server_error(request, exception=None):
    context = {
        'title': 'Server error',
        'text': 'Sorry the server is unavailable',
        'code': 500
    }
    return render(request, 'CustomAuth/pages/status.html', context=context)


def permission_denied(request, exception=None):
    context = {
        'title': 'Forbidden',
        'text': 'Permission Denied',
        'code': 403
    }
    return render(request, 'CustomAuth/pages/status.html', context=context)


def unauthorized(request, exception=None):
    context = {
        'title': 'Unauthorized',
        'text': 'Unauthorized',
        'code': 401
    }
    return render(request, 'CustomAuth/pages/status.html', context=context)


def bad_request(request, exception=None):
    context = {
        'title': 'Bad request',
        'text': 'Bad request',
        'code': 400
    }
    return render(request, 'CustomAuth/pages/status.html', context=context)


def maintenance(request, exception=None):
    context = {
        'title': 'Server on Maintenance',
        'text': "Sorry we're down for maintenance",
        'code': 503
    }
    return render(request, 'CustomAuth/pages/status.html', context=context)
