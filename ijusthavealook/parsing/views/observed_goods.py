from django.shortcuts import render
from django.views.generic import TemplateView

from . import menu

from parsing.models import Observed, Goods, ConcurentGoods, Context, Prices, ConcurentPrices


class ObservedGoodsView(TemplateView):
    template_name = 'parsing/observed_goods.html'

    def get(self, request, observed_id: int):
        our_company = Context.objects.get(pk=1)
        goods_prices = []
        if our_company.pk == observed_id:
            goods = Goods.objects.all()
            for good in goods:
                good_prices = [price for price in Prices.objects.filter(good_id=good).order_by('-date')]
                goods_prices.append({
                    'good': good,
                    'prices': good_prices
                })
        else:
            goods = ConcurentGoods.objects.filter(company=observed_id)
            for good in goods:
                good_prices = [price for price in ConcurentPrices.objects.filter(good_id=good).order_by('-date')]
                goods_prices.append({
                    'good': good,
                    'prices': good_prices
                })
        observed_name = Observed.objects.get(pk=observed_id)
        context = {
            'title': 'Список товаров',
            'menu': menu,
            'observed_name': observed_name,
            'goods_prices': goods_prices
            }

        return render(request, self.template_name, context)