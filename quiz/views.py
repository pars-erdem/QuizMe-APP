from django.shortcuts import render
from .models import Question, Topic

# Template Views
def index(request):
    return render(request, 'index.html')

def ai_quiz(request):
    q_obj = Question.objects.filter(topic='ARTIFICIAL INTELLIGENCE')
    q_context = {'questions': q_obj}
    return render(request, 'ai_quiz.html', q_context)

def cyber_quiz(request):
    q_obj = Question.objects.filter(topic='CYBER_SECURITY')
    q_context = {'questions': q_obj}
    return render(request, 'cyber_quiz.html', q_context)

def backend_quiz(request):
    q_obj = Question.objects.filter(topic='BACKEND')
    q_context = {'questions': q_obj}
    return render(request, 'backend_quiz.html', q_context)

def mobile_quiz(request):
    q_obj = Question.objects.filter(topic='MOBILE')
    q_context = {'questions': q_obj}
    return render(request, 'mobile_quiz.html', q_context)

