""" Extra tags filter for the webSite app """
from django import template
import random

register = template.Library()


@register.simple_tag
def randint(a, b=None):
    """Function to get a random

    Arguments:
        value {dict} -- The dict used

    Returns:
        lenght {int} -- The lenght of all the list of the dict
    """
    if b is None:
        a, b = 0, a
    return random.randint(a, b)
