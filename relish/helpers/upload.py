# -*- coding: utf-8 -*-
import os
import random
import string
import datetime
from django.conf import settings
from django.utils.encoding import force_str, force_text

path_dict = getattr(settings, 'IMAGE_UPLOAD_TO', {})


def upload_to(path):
    """
    Generates unique ascii filename before saving. Supports strftime()
    formatting as django.db.models.FileField.upload_to does.

    Example:

        class SomeModel(models.Model):
            picture = models.ImageField(upload_to=upload_to('my_model_uploads/'))

    It is possible to define `upload_to` folder depending on model.
    Declare dict `IMAGE_UPLOAD_TO` in settings:
    {
        'ModelName': 'path for upload_to"',
    }
    And provide None to upload_to func as path.
    """
    def upload_callback(instance, filename):
        random_fname = ''.join(
            random.choice(string.ascii_uppercase + string.digits) for x in range(16))
        random_fname += os.path.splitext(filename)[-1]
        if path is None:
            img_path = path_dict.get(instance.__class__.__name__, "images")
        else:
            img_path = path
        img_path = os.path.normpath(force_text(
            datetime.datetime.now().strftime(force_str(img_path))))
        return '%s/%s' % (img_path.rstrip('/'), random_fname)
    return upload_callback
