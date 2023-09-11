from django import template
from django.db.models import OuterRef, Subquery, F

from parsing.models import Observed, Goods, Prices, ConcurentPrices, ConcurentGoods, Context


register = template.Library()


@register.simple_tag(name='getobs')
def get_observed():
    return Observed.objects.all()


@register.simple_tag(name='getgoods')
def get_goods():
    return Goods.objects.all().select_related()

@register.simple_tag(name='getgoodbyid')
def get_good_by_id(good_id: int):
    return Goods.objects.get(pk=good_id)

@register.simple_tag(name='getlastprices')
def get_last_prices(observed_id: int = None):
    pass

    # observed = None
    # if observed_id:
    #     subquery = Prices.objects.filter(good_id=OuterRef('good_id')).order_by('-date')
    #     latest_prices = Prices.objects.filter(
    #         observed_id_id=observed_id,
    #         date=Subquery(subquery.values('date')[:1])
    #     )
    #     observed = Observed.objects.get(pk=observed_id)
    #     queryset = latest_prices.annotate(
    #         name=Subquery(Goods.objects.filter(pk=OuterRef('good_id')).values('name')[:1])
    #     ).values('name', 'price', 'date', 'good_id')
    # else:
    #     queryset = Prices.objects. \
    #         select_related(). \
    #             values('good_id', 'good_id__name'). \
    #                 annotate(name=F('good_id__name')). \
    #                     distinct()

    # return {'goods': queryset, 'observed': observed}
    