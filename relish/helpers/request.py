# -*- coding: utf-8 -*-

def get_client_ip(request):
    """
    Returns client ip from request.
    Source: http://stackoverflow.com/a/4581997/821594
    """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def get_client_browser(request):
    """
    Returns client browser
    """
    return request.META.get('HTTP_USER_AGENT')
