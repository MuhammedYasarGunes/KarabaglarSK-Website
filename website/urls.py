from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('', views.index, name='index'),
    path('galeri/', views.galeri, name='galeri'),
    path('takim/', views.takim, name='takim'),
    path('maclar/', views.maclar, name='maclar'),
    path('iletisim/', views.iletisim, name='iletisim'),
]
