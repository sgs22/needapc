from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.views.generic import DetailView

from .models import Quiz, Question, Choice, QuizAnswer, User

from .forms import AnswerForm
from django.forms import modelformset_factory, inlineformset_factory


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

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     quiz_id = context.get('object').id
    #     context['question_list'] = Question.objects.select_related().filter(quiz=quiz_id)
    #     context['question_list2'] = Question.objects.select_related()
    #     number_of_questions = len(Question.objects.select_related().filter(quiz=quiz_id))
    #     # print(context['question_list'])
    #     # form_list = []
    #     # for question in context['question_list']:
    #     #     form = AnswerForm(question=question.id)
    #     #     context[f'form{question.id}'] = form
    #     #     form_list.append(context[f'form{question.id}'])
    #     #     print(f'form{question.id}')
    #     # print(form_list)

    #     # print(formset)
    #     # context['formset'] = formset
    #     return context

def quiz_detail(request, slug):
    template_name = 'quizApp/quiz_detail.html'
    quiz = get_object_or_404(Quiz, slug=slug)
    questions = quiz.questions.all()
    return render(request, template_name, {'quiz': quiz,
                                            'question_list':questions})
        
class QuestionList(generic.ListView):
    queryset = Question.objects.all()
    template_name = 'quizApp/question.html'
    context_object_name = 'question_list'

class QuestionDetail(generic.DetailView):
    model = Question
    template_name = 'quizApp/question_detail.html'

def question_detail(request, slug, pk):
    quiz = get_object_or_404(Quiz, slug=slug)
    template_name = 'quizApp/question_detail.html'
    question = Question.objects.get(pk=pk)
    next_question = int(question.question_order) + 1
    choices = question.choices.all()
    if request.method == 'POST':
        print(request.POST)
        form = AnswerForm(request.POST, choices=choices)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.user = request.user
            form.save()
            # if next question exists then redirect it
            # else get result page
            return redirect('quizApp:question_detail', slug=slug, pk=next_question)
    else:
        form = AnswerForm(choices=choices)
    return render(request, template_name, {'question': question,
                                            'choices':choices,
                                            'form':form})





# for each question in quiz:
    # for each choice in question:
        # formset init set_related


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


