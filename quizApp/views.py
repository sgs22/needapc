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
        # print(context)
        # print(context.get('object').slug)
        # print(context.get('object'))
        # print(Question.objects.first())
        quiz_id = context.get('object').id
        # Add in a QuerySet of all the questions
        context['question_list'] = Question.objects.select_related().filter(quiz=quiz_id)
        context['choice_list'] = Choice.objects.all()
        question_id = context.get('object').id
        #for question in context['question_list']:
        #    print(question.question_choices.all().values())
            # context['question_choices'] = question.choice_set.all()

        # print(context['question_list'].id)
        # question = context['question_list'].values.id
        # context['choice_list'] = Choice.objects.select_related()
        # print(context['choice_list'])

        # reverse lookup - question.choice_set.all() gets all related choices to that question
        # context['choice_list_reverselookup'] = question_choices.values()
        form = AnswerForm()
        context['form'] = form
        return context

# def get_answer(request):
#     if request.method == 'POST':
#         form = AnswerForm(request.POST)
#         if form.is_valid():
#             return  HttpResponseRedirect('/thanks/')
#     else:
#         form = AnswerForm()
#     return render(request, 'answer.html', {'form': form})
