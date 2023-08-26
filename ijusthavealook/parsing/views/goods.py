from django.shortcuts import render
from django.views.generic import TemplateView

from .index import menu


class GoodsListView(TemplateView):
    template_name = 'parsing/goods.html'

    def get(self, request):

        context = {
            'title': 'Goods list',
            'menu': menu,
            }

        return render(request, self.template_name, context)