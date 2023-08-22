from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q
from django.views.generic import TemplateView

from parsing.models import Goods, Prices, Observed


class PricesView(TemplateView):
    template_name = 'parsing/prices.html'

    def get(self, request):
        observed = Observed.objects.all()
        context= { 'title': 'Prices page', 'observed': observed }

        return render(request, self.template_name, context)    
