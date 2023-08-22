from django import template
from parsing.models import Observed

register = template.Library()


@register.simple_tag(name='getobs')
def get_observed():
    return Observed.objects.all()