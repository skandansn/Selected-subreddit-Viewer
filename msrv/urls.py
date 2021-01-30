from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name='home'),
    path('searchfields', views.searchfields,name='searchfields'),
]
