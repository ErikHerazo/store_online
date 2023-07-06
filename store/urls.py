from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    path('index/', views.index, name='index'),
]