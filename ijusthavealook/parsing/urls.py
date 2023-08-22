from django.urls import path

from parsing.views.main_page import IndexView
from parsing.views.prices import PricesView
from parsing.views.good_prices import GoodPricesView


urlpatterns = [
    path('', IndexView.as_view()),
    path('prices/', PricesView.as_view()),
    path('prices/<str:good_id>/', GoodPricesView.as_view())
]


