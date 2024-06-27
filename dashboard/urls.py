from django.urls import path
from .views import display_ticker
from dashboard import views

app_name = "dashboard"
urlpatterns = [
    path('',views.home, name='home'),
    path('stockhome/', views.stockhome, name='stockhome'),
    path("<str:ticker>/", display_ticker, name="display_ticker"),
    path('main/', views.main_page, name='main'),
]