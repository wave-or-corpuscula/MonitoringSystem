from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Магазины', 'url_name': 'observed'},
    {'title': 'Товары', 'url_name': 'goods'},
]


class IndexView(TemplateView):
    template_name = 'parsing/index.html'

    def get(self, request):

        context = {
            'title': 'Wealcome', 
            'menu': menu
            }

        return render(request, self.template_name, context)

