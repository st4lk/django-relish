from django.http import HttpResponseRedirect
from django.shortcuts import resolve_url
from functools import wraps
from django.conf import settings
from django.utils.decorators import available_attrs


def anonimous_required(view_func):
    """
    Reverse for django.contrib.auth.decorators.login_required
    When applied, it checks, that user is anonimous.
    If not, it redirects to `settings.LOGIN_REDIRECT_URL` url.
    Example:
        url(r'^$', anonimous_required(
            TemplateView.as_view(template_name="home.html"))),
    """
    @wraps(view_func, assigned=available_attrs(view_func))
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect(resolve_url(settings.LOGIN_REDIRECT_URL))
        else:
            return view_func(request, *args, **kwargs)
    return _wrapped_view
