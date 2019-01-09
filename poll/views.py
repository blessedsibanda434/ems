from django.shortcuts import render

def index(request):
    context = {}
    context['title'] = 'polls'
    return render(request, 'polls/index.html', context)
