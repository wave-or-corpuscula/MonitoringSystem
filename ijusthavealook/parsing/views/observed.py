from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from . import menu


class ObservedListView(TemplateView):
    template_name = 'parsing/observed.html'

    def get(self, request):
        context = {
            'title': 'Observed sotres list',
            'menu': menu
            }

        return render(request, self.template_name, context)