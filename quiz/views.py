from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Quiz, Question, Choice, QuizTakers

from .forms import MyForm

'''
    TODO: want to get questions for quizes that are active
'''

def answer(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = MyForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/quiz/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = MyForm()

    return render(request, '/quiz/quiz.html', {'form': form})


class QuizView(generic.ListView):
    template_name = 'quiz/quiz.html'
    context_object_name = 'question_list'

    def get_queryset(self, *args, **kwargs):
        
        #get questions for active quiz only?
        queryset = Question.objects.all()
        return queryset
        
class DetailView(generic.DetailView):
    model = Question
    template_name = 'quiz/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'quiz/results.html'


def question_view(request):
    question_list = Question.objects.order_by('pub_date')
    return render(request, "quiz/quiz.html", {'question_list': question_list})

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'quiz/detail.html', {'question': question})

def choice_view(request, id=None, *args, **kwargs):
    choice_list = Choice.objects.all()
    return render(request, "quiz/quiz.html", {"choice_list": choice_list})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'quiz/results.html', {'question': question})

# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'quiz/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('quiz:results', args=(question.id,)))

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id) # gets current question
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice']) #gets selected choice
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'quiz/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else: #update model
        user_answer.question = question
        user_answer.answer = selected_choice
        selected_choice.save()
        user_answer.save()
        
        
        
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('quiz:results', args=(question.id,)))

def select_answer(request, question_id):
    question = get_object_or_404(Question, pk=question_id) # gets current question

    selection = request.POST('choice')





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