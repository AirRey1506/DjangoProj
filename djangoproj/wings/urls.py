from django.urls import path
from wings.views import *
app_name = 'wings'
urlpatterns = [
    path('home', index, name='index'),
    path('testlang', testlang, name='testlang'),
    path('openPrice', openPrice, name='openPrice'),
]

