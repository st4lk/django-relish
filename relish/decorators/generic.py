from functools import wraps
"""
wraps helps to remember information about wrapped function,
for example attributes like __name__, __doc__
details: http://docs.python.org/2/library/functools.html#functools.wraps
"""


def instance_cache(func):
    """
    Stores returned value as instance attr.
    Currently function arguments are not respected, i.e. result of first
    call will always be returned.

    Usage example:

        from relish.decorators import instance_cache

        class MyModel(models.Model):
            name = models.CharField(max_length=20)

            @instance_cache
            def first_another(self):
                # heavy calculation goes here
                # or hitting the database
                return AnotherModel.objects.all()[0]

        my = MyModel.objects.get(id=1)

        my.first_another() # hits database and saves as instance attr
        my.first_another() # got from instance saved attr
        my.first_another() # got from instance saved attr

    Can be used with @property decorator:

        class MyModel(models.Model):
            # ...

            @property
            @instance_cache
            def first_another(self):
                # ...

        my = MyModel.objects.get(id=1)

        print my.first_another
    """

    @wraps(func)
    def wrapped(instance, *args, **kwargs):
        attr_name = "_{0}".format(func.__name__)
        if hasattr(instance, attr_name):
            return getattr(instance, attr_name)
        else:
            value = func(instance, *args, **kwargs)
            setattr(instance, attr_name, value)
            return value
    return wrapped


def self_if_blank_arg(func):
    """
    If all of function args and kwargs are False in python way, then
    return self. Otherwise, return applied function. Useful for querysets.

    Example:

        from relish.decorators import self_if_blank_arg

        class MyModel(QuerySet):
            # to apply this queryset to model use PassThroughManager 
            # from django-model-utils
            # or see https://code.djangoproject.com/ticket/15062 for 
            # solution without dependencies

            @self_if_blank_arg
            def in_country(self, country):
                return self.filter(country=country)


        # `country` variable contains country or None
        # If None, country filter will NOT be applied
        MyModel.objects.in_country(country)
    """

    @wraps(func)
    def wrapped(instance, *args, **kwargs):
        if any(args) or any(kwargs.values()):
            return func(instance, *args, **kwargs)
        else:
            return instance
    return wrapped
