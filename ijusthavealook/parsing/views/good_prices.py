from django.db.models import F
from django.shortcuts import render
from django.views.generic import TemplateView

from parsing.models import Goods, Prices, Observed, ConcurentGoods, ConcurentPrices


from . import menu


class GoodPricesView(TemplateView):
    template_name = 'parsing/good_prices.html'

    def get(self, request, good_id: str):

        contains = []
        contains.append({
            'observed': Observed.objects.get(pk=Goods.objects.get(pk=good_id).observed_id.pk),
            'prices': Prices.objects.filter(good_id=good_id).order_by('-date')
        })

        related_goods = ConcurentGoods.objects.filter(origin_good_id=good_id)
        for good in related_goods:
          contains.append({
            'observed': good.company,
            'prices': ConcurentPrices.objects.filter(good_id=good.pk).order_by('-date')
        })  
        
        context = {
            'title': 'Цены товара',
            'menu': menu,
            'good_id': good_id,
            'contains': contains
        }
    
        return render(request, 
                      self.template_name, 
                      context=context
                      )
    