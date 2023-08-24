from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from .index import menu


class AboutView(TemplateView):
    template_name = 'parsing/about.html'

    def get(self, request):
        context = {
            'title': 'About page',
            'menu': menu
            }

        return render(request, self.template_name, context)
    