from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from .index import menu

from parsing.models import ConcurentGoods


class SetOriginView(TemplateView):
    template_name = 'parsing/set_origin.html'

    def get(self, request, good_id: int):

        void_goods = ConcurentGoods.objects.filter(origin_good_id__isnull=True).select_related()
        # for good in void_goods:
        #     print(good.name, good.company, good.origin_good_id)
        context = {
            'title': 'Добавить товар',
            'menu': menu,
            'good_id': good_id,
            'void_goods': void_goods
            }

        return render(request, self.template_name, context)
    

def add_origin_to_good(request):
    if request.method == 'GET':
        origin_id = request.GET.get('origin_id')
        correspond_good_ids = request.GET.get('correspond_good_ids')

        cor_good_ids = correspond_good_ids.split(',');

        print(cor_good_ids)

        return JsonResponse({'prices': 'prices_data'})
