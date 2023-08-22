from datetime import datetime

from django.http import JsonResponse
from django.shortcuts import render
from django.db.models import Q
from django.views.generic import TemplateView

from parsing.models import Goods, Prices, Observed


class PricesView(TemplateView):
    template_name = 'parsing/prices.html'

    def get(self, request):
        context= { 'title': 'Prices page'}

        return render(request, self.template_name, context)    


def get_goods_data(request):
    if request.method == 'GET':
        store_id = request.GET.get('store_id')  # Получаем ID магазина из параметра
        if store_id:
            prices = Prices.objects.filter(observed_id=store_id)
            prices_data = [{'good_id': price.good_id_id, 'price': price.price} for price in prices]
            return JsonResponse({'prices': prices_data})
        else:
            return JsonResponse({'error': 'Store ID not provided'})
