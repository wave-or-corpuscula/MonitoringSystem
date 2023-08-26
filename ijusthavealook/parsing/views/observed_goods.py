from django.shortcuts import render
from django.views.generic import TemplateView

from .index import menu


class ObservedGoodsView(TemplateView):
    template_name = 'parsing/goods.html'

    def get(self, request, observed_id: int):

        context = {
            'title': 'Goods list',
            'menu': menu,
            'observed_id': observed_id
            }

        return render(request, self.template_name, context)