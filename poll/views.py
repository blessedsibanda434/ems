from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from poll.models import Question, Answer, Choice

def index(request):
    context = {}
    questions = Question.objects.all()
    context['title'] = 'polls'
    context['questions'] = questions
    return render(request, 'polls/index.html', context)


def details(request, id=None):
    question = get_object_or_404(Question, id=id)
    context = {
        'question': question
    }
    return render(request, 'polls/details.html', context)

def poll(request, id=None):
    if request.method == "GET":
        question = get_object_or_404(Question, id=id)
        context = {
            'question': question
        }
        return render(request, 'polls/poll.html', context)

    if request.method == "POST":
        user_id = 1
        data = request.POST 
        ret = Answer.objects.create(user_id=user_id, choice_id=data['choice'])
        if ret:
            return HttpResponse("Your vote is done successfully")
        else:
            return HttpResponse("Your vote is not done successfully")