from django.contrib.sites.models import get_current_site

def get_domain(request=None):
    return "http://" + str(get_current_site(request))
