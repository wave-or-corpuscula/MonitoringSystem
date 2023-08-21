from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q

from parsing.models import Goods, Prices, Observed


def prices(request, good_id: str):

    try:
        good = Goods.objects.get(id=good_id)
    except Exception:
        return HttpResponse(f'<h1>No goods with such id</h1>')    
    
    prices = Prices.objects.filter(
        Q(date__date=datetime(2023, 8, 19)),
        good_id=good_id).select_related()
    if len(prices) == 0:
        return HttpResponse(f'<h1>No price for your good</h1>')
    print(prices[0].date)

    response = f'Prices on good: {good.name}:<br>'
    response += '<br>'.join([f'{p.observed_id}: {p.price}' for p in prices])
    
    observed = Observed.objects.all()

    return render(request, 
                  'parsing/prices.html', 
                  context={
                      'title': 'Prices page',
                      'observed': observed
                  })

    # return HttpResponse(response)
