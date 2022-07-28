from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import DetailView

from .models import Quiz, Question, Choice, QuizAnswer, User

from .forms import AnswerForm
from django.forms import modelformset_factory


class QuizList(generic.ListView):
    queryset = Quiz.objects.all()
    template_name = 'quizApp/quiz.html'
    context_object_name = 'quiz_list'


class QuizDetail(generic.DetailView):
    model = Quiz
    template_name = 'quizApp/quiz_detail.html'

    # def form_valid(self, form):
    #     form = form.save(commit=False)
    #     form.user = User.objects.get(user=self.request.user)
    #     form.save()
    #     print(form.user)
    #     return redirect('quizapp/')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        quiz_id = context.get('object').id
        context['question_list'] = Question.objects.select_related().filter(quiz=quiz_id)
        number_of_questions = len(Question.objects.select_related().filter(quiz=quiz_id))
        print(context['question_list'])
        form_list = []
        # for question in context['question_list']:
        #     form = AnswerForm(question=question.id)
        #     context[f'form{question.id}'] = form
        #     form_list.append(context[f'form{question.id}'])
        #     print(f'form{question.id}')
        # print(form_list)
        context['form_list'] = form_list

        AnswerFormSet = modelformset_factory(QuizAnswer, fields='__all__', extra=number_of_questions)
        formset = AnswerFormSet(queryset=Choice.objects.filter(id=1))
        # initial=[{'answer_choice': Choice.objects.filter(id=question),'user': 2,} for question in [1,3]]
        print(formset)
        context['formset'] = formset
        return context


# for question in context['question_list']:
#    print(question.question_choices.all().values())
# context['question_choices'] = question.choice_set.all()

# print(context['question_list'].id)
# question = context['question_list'].values.id
# context['choice_list'] = Choice.objects.select_related()
# print(context['choice_list'])

# reverse lookup - question.choice_set.all() gets all related choices to that question
# form = AnswerForm(question=question_id)
# context['form'] = form

# def get_answer(request):
#     if request.method == 'POST':
#         form = AnswerForm(request.POST)
#         if form.is_valid():
#             return  HttpResponseRedirect('/thanks/')
#     else:
#         form = AnswerForm()
#     return render(request, 'answer.html', {'form': form})


