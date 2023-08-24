from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from .index import menu
from parsing.models import Goods


class GoodsListView(TemplateView):
    template_name = 'parsing/goods.html'

    def get(self, request):
        goods = Goods.objects.all()

        context = {
            'title': 'Goods list',
            'menu': menu,
            'goods': goods
            }

        return render(request, self.template_name, context)