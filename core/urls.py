from django.urls import path
from .views import *



urlpatterns = [
    path('', index, name='index'),
    path('contato/', contato, name='contato'),
    path('produtos/', produtos, name='produtos'),
    path('accounts/login/', LoginView.as_view(), name='login'),
]