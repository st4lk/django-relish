from django.contrib.sites.models import get_current_site
from django.conf import settings


def get_domain(request=None, protocol=None):
    protocol = protocol or getattr(settings, "SITE_PROTOCOL", None) or 'http'
    return "{0}://{1}".format(protocol, get_current_site(request))
