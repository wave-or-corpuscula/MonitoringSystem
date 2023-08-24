from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from .index import menu
from parsing.models import Goods, Observed, Prices


class ObservedGoodsView(TemplateView):
    template_name = 'parsing/goods.html'

    def get(self, request, observed_id: int):
        good_ids = Prices.objects.filter(observed_id=observed_id).distinct().values_list('pk')
        print(good_ids)
        goods = Goods.objects.filter(id__in=good_ids)
        observed = Observed.objects.get(pk=observed_id)
        print(goods)

        context = {
            'title': 'Goods list',
            'menu': menu,
            'goods': goods,
            'observed': observed.name
            }

        return render(request, self.template_name, context)