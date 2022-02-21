from django.shortcuts import render
from django.views import generic
from django.views.generic import DetailView

from .models import Quiz, Question, Choice, QuizAnswer

from .forms import AnswerForm


class QuizList(generic.ListView):
    queryset = Quiz.objects.all()
    template_name = 'quizApp/quiz.html'
    context_object_name = 'quiz_list'

class QuizDetail(generic.DetailView):
    model = Quiz
    template_name = 'quiz/quiz_detail.html'

# def get_answer(request):
#     if request.method == 'POST':
#         form = AnswerForm(request.POST)
#         if form.is_valid():
#             return  HttpResponseRedirect('/thanks/')
#     else:
#         form = AnswerForm()
#     return render(request, 'answer.html', {'form': form})
