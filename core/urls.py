from django.urls import path
from .views import contato,index

urlpatterns = [
    path('', index, name='index'),
    path('contato/', contato, name='contato'),

]