from django.urls import path

from parsing.views.main_page import index
from parsing.views.prices import prices


urlpatterns = [
    path('', index),
    path('prices/<str:good_id>/', prices)
]


