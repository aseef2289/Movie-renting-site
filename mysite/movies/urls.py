from django.urls import path
from . import views
from . import viewz

app_name = 'movies'

urlpatterns = [
    path('', viewz.home),
    path('', views.index, name='index'),
    path('<int:movie_id>', views.detail, name='detail')
]