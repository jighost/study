from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('wc_board', views.wc_board, name='wc_board'),
    path('im', views.im, name='im'),
]