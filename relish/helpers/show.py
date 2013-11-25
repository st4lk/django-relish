# -*- coding: utf-8 -*-

def show_age_ru(age):
    """
    Shows correct age (russian language)
    """
    last_age_digit = age % 10
    if last_age_digit == 1:
        unit = u'год'
    elif last_age_digit >= 2 and last_age_digit <= 4:
        unit = u'года'
    else:
        unit = u'лет'
    return u"{0} {1}".format(age, unit)
