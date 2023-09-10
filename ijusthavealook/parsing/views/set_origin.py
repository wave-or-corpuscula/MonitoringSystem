from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from . import menu

from parsing.models import ConcurentGoods, Goods


class SetOriginView(TemplateView):
    template_name = 'parsing/set_origin.html'

    def get(self, request, good_id: int):

        void_goods = ConcurentGoods.objects.filter(origin_good_id__isnull=True).select_related()
        context = {
            'title': 'Добавить товар',
            'menu': menu,
            'good_id': good_id,
            'void_goods': void_goods
            }

        return render(request, self.template_name, context)
    

def add_origin_to_good(request):
    print(request)
    if request.method == 'GET':
        origin_id = request.GET.get('origin_id')
        print(origin_id)
        correspond_good_ids = request.GET.get('correspond_good_ids')

        cor_good_ids = correspond_good_ids.split(',');

        cor_goods = ConcurentGoods.objects.filter(pk__in=cor_good_ids)
        for good in cor_goods:
            good.origin_good_id = Goods.objects.get(pk=origin_id)
            good.save()

        return JsonResponse({'prices': 'prices_data'})
