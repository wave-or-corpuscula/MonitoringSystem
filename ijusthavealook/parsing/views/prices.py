from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q

from parsing.models import Goods, Prices, Observed


def prices(request):
    
    observed = Observed.objects.all()

    return render(request, 
                  'parsing/prices.html', 
                  context={
                      'title': 'Prices page',
                      'observed': observed
                  })