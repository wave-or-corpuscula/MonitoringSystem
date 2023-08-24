from django.urls import path

from parsing.views import *


urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('prices/', PricesView.as_view(), name='prices'),
    path('about/', AboutView.as_view(), name='about'),
    path('observed/', ObservedListView.as_view(), name='observed'),
    path('observed/<int:observed_id>/', ObservedGoodsView.as_view()),
    path('goods/', GoodsListView.as_view(), name='goods'),
    path('prices/<int:good_id>/', GoodPricesView.as_view(), name='good_prices'),

    path('get_goods_data/', get_goods_data)
]


