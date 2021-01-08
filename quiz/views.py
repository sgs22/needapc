from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, Http404


from .models import Question, Choice

def question_view(request):
    question_list = Question.objects.order_by('pub_date')
    return render(request, "quiz/quiz.html", {'question_list': question_list})

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'quiz/detail.html', {'question': question})

def choice_view(request, id=None, *args, **kwargs):
    choice_list = Choice.objects.all()
    return render(request, "quiz/quiz.html", {"choice_list": choice_list})



# Create your views here. ____________________________________________________________



# def question_view(request, question_id):
#     try:
#         q = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'quiz/quiz.html', {'question': q})

# def choice_view(request, choice_id):
#     try:
#         q = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'quiz/quiz.html', {'question': q})