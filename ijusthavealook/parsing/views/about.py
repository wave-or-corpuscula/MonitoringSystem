from django.shortcuts import render
from django.views.generic import TemplateView

from . import menu


class AboutView(TemplateView):
    template_name = 'parsing/about.html'

    def get(self, request):
        context = {
            'title': 'About page',
            'menu': menu
            }

        return render(request, self.template_name, context)
    