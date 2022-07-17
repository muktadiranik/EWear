from django import template
from django.contrib.humanize.templatetags.humanize import intcomma

register = template.Library()


@register.filter(name='currency')
def currency(number):
    return '$ ' + str(number)
