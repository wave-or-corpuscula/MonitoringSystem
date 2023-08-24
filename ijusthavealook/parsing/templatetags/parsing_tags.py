from django import template
from parsing.models import Observed, Goods

register = template.Library()


@register.simple_tag(name='getobs')
def get_observed():
    return Observed.objects.all()


@register.simple_tag(name='getgoods')
def get_goods():
    return Goods.objects.all().select_related()