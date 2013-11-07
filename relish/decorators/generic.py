from functools import wraps

def instance_cache(func):
    """
    Stores returned value as instance attr.
    Currently function arguments are not respected, i.e. result of first
    call will always be returned.

    Usage example:

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
