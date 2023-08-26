from django.db.models import F
from django.shortcuts import render
from django.views.generic import TemplateView

from parsing.models import Goods, Prices, Observed


from .index import menu


class GoodPricesView(TemplateView):
    template_name = 'parsing/good_prices.html'

    def get(self, request, good_id: str):

        contains = []
        contains_stores = Prices.objects. \
            filter(good_id=good_id). \
                select_related(). \
                    values("observed_id"). \
                        distinct(). \
                            annotate(observed_name=F('observed_id__name'))
        for store in contains_stores:
            observed_id = store.get('observed_id')
            prices = Prices.objects. \
                filter(observed_id=observed_id, good_id=good_id). \
                    values('price', 'date'). \
                        order_by('-date')
            contains.append({
                'observed_id': observed_id, 
                'observed': store.get('observed_name'), 
                'prices': prices
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
    