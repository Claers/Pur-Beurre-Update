""" Extra tags filter for the webSite app """
from django import template

import urllib.parse as parser
from django.contrib.admin.utils import quote
register = template.Library()


def dictLenght(value):
    """Function filter to calculate the lenght of all list inside of a dict

    Arguments:
        value {dict} -- The dict used

    Returns:
        lenght {int} -- The lenght of all the list of the dict
    """
    if isinstance(value, dict):
        lenght = 0
        for keys in value:
            for val in value[keys]:
                lenght += 1
    return lenght


register.filter('dictLenght', dictLenght)
