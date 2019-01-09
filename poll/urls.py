from django.urls import path 
from poll.views import index

urlpatterns = [
    path('', index, name='polls_list'),
]