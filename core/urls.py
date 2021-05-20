from django.urls import path
from core.views import load, form, result

urlpatterns = [
    path('load/', load),
    path('form/', form),
    path('result/', result, name='result'),
]