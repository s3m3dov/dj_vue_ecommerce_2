from django.urls import path

from .views import LatestProductList


urlpatterns = [
    path('latest-products/', LatestProductList.as_view()),
]