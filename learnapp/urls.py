from django.urls import path
from . import views

urlpatterns = [
    path('', views.myfunctioncall, name='index'),
    path('about', views.myfunctionabout, name='about'),
    path('add/<int:a>/<int:b>', views.add, name='add'),
    path('intro/<str:name>/<int:age>', views.intro, name='intro'),
    path('firstpage', views.firstpage, name='firstpage'),
    path('second', views.second, name='second'),
    path('third', views.third, name='third'),
path('ipage2', views.ipage2, name='ipage2'),
    path('ipage', views.ipage, name='ipage'),
path('ipage3', views.ipage3, name='ipage3'),
path('ipage4/<str:imagename>', views.ipage4, name='ipage4'),
    path('forms', views.forms, name='forms'),
    path('sforms', views.sforms, name='sforms'),
    path('forms2', views.forms2, name='forms2')
]