from django.urls import path

from parsing.views.main_page import index
from parsing.views.prices import prices
from parsing.views.good_prices import good_prices


urlpatterns = [
    path('', index),
    path('prices/', prices),
    path('prices/<str:good_id>/', good_prices)
]


