from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'parsing/index.html'

    def get(self, request):

        context = {'title': 'Wealcome' }

        return render(request, self.template_name, context)


def index(request):
    return render(request, 
                  'parsing/index.html',
                  context={
                      'title': 'Welcome'
                  })