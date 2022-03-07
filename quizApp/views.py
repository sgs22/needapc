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
    template_name = 'quizApp/quiz_detail.html'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        print(context)
        print(context.get('object'))
        # print(Question.objects.first())
        quiz = context.get("quiz")
        # Add in a QuerySet of all the questions
        context['question_list'] = Question.objects.filter(quiz__exact=1) #get questions where quiz = this.quiz
        return context

# def get_answer(request):
#     if request.method == 'POST':
#         form = AnswerForm(request.POST)
#         if form.is_valid():
#             return  HttpResponseRedirect('/thanks/')
#     else:
#         form = AnswerForm()
#     return render(request, 'answer.html', {'form': form})
