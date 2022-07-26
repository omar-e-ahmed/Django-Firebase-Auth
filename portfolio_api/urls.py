from django.contrib import admin
from django.urls import path
from portfolio_api.views import PortfolioCreate, PortfolioList, PortfolioDetails

urlpatterns = [
    path('list', PortfolioList.as_view()),
    path('', PortfolioCreate.as_view()),
    path('<int:pk>', PortfolioDetails.as_view()),

]
