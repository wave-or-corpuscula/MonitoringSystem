from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from . import menu


class IndexView(TemplateView):
    template_name = 'parsing/index.html'

    def get(self, request):

        context = {
            'title': 'Wealcome', 
            'menu': menu
            }

        return render(request, self.template_name, context)

