from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404


from .models import Question, Choice

def question_view(request):
    question_list = Question.objects.all()
    return render(request, "quiz/quiz.html", {"question_list": question_list})

def choice_view(request):
    choice_list = Choice.objects.all()
    return render(request, "quiz/quiz.html", {"choice_list": choice_list})

# Create your views here.

# def quiz_view(request, id=None, *args, **kwargs):
#     return render(request, "quiz/quiz.html")

# def question_view(request, id=None, *args, **kwargs):
#     questionquery = Question.objects.all()
#     return render(request, "quiz/quiz.html", {"question_query": questionquery})

# def choice_view(request, id=None, *args, **kwargs):
#     choicequery =  Choice.objects.all()
#     return render(request, "quiz/quiz.html", {"choice_query": choicequery})

# def quiz_view(request, id=None, *args, **kwargs):
#     queryset = FeaturedPost.objects.filter(status=1).order_by('-created_on')
#     return render(request, "featured/featured.html", {"featured_list": queryset})

# return render(request, "featured/featured.html", {"quiz_list": queryset})


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