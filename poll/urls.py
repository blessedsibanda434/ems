from django.urls import path 
from poll.views import index, details, poll

urlpatterns = [
    path('', index, name='polls_list'),
    path('<int:id>/details', details, name='poll_details'),
    path('<int:id>/', poll, name='single_poll'),
]