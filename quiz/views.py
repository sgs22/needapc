from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from products.models import ProductDetail

from .models import Quiz, Question, Choice, UserResponse, Application

from .forms import ResponseForm

'''
    List of all available "quizzes"
'''
class QuizList(generic.ListView):
    queryset = Quiz.objects.filter(active=True).order_by('id')
    template_name = 'quiz/quiz.html'

class QuizDetail(generic.DetailView):
    model = Quiz
    template_name = 'quiz/quiz_detail.html'
'''
    single quiz view
'''
@login_required
def quiz_detail(request, slug):
    template_name = 'quiz/quiz_detail.html'
    quiz = get_object_or_404(Quiz, slug=slug)
    if request.method == 'POST':
        form = ResponseForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('/quiz/laptops/overview') #will be changed to results page needs dynamic url
    else:
        form = ResponseForm()
    return render(request, template_name, {'quiz':quiz,
                                           'form': form})
#get response for this user user.request


# def results_view(request, *args, **kwargs):
#     questions = Question.objects.filter(quiz__title="Laptop")
#     responses = UserResponse.objects.filter(user=request.user).order_by('-id')[:1] #last object
#     return render(request, "quiz/results.html", {'responses': responses,
#                                                 'questions': questions})

'''
    Presents user with the choices they made in the quiz
    then:     - users responses so that logic can be performed for user results (converts querysets to str/int)
              - logic performed on each response     
              - TODO: import products to filter them based on responses using products attributes
                        e.g. if user responds to question saying they will commute a lot then weight of 
                                products should be less than x kilos (<2kgs)

'''
def overview_view(request, *args, **kwargs):
    questions = Question.objects.filter(quiz__title="Laptop")
    responses = UserResponse.objects.filter(user=request.user).order_by('-id')[:1] #last object placed into db
    return render(request, "quiz/overview.html", {'responses': responses,
                                                'questions': questions})

def results_view(request, *args, **kwargs):
    response_1 = UserResponse.objects.filter(user=request.user).order_by('-id')[:1].values_list('response_1', flat=True).get()
    response_2 = UserResponse.objects.filter(user=request.user).order_by('-id')[:1].values_list('response_2', flat=True).get()
    response_3 = UserResponse.objects.filter(user=request.user).order_by('-id')[:1].values_list('response_3', flat=True).get()
    print(int(response_1),response_2, response_3) #logic for filtering out products based on user budget input
    
    #HARD CODED REPOSNSES DIRECTLY LINKED TO QUESTION INPUT
    #will return 3 products from db currently only filter based on price and return 3 products
    if int(response_1) < 350:
        print("recommend going used")
    else:
        print("fail")
    result = ProductDetail.objects.filter(price__lte=response_1)[:3] #budget
    result_2 = ProductDetail.objects.filter(weight__lte=response_2)[:3] #weight
    result_2 = ProductDetail.objects.filter(weight__lte=response_2)[:3] #display (resolution)
    print(result)
    return render(request, "quiz/results.html", {'results': result})


    #budget
    #apps (performance)
    #weight 
    #battery
    #design
    #storage
    #ports?
    
    



# def results(request, question_id):
# question = get_object_or_404(Question, pk=question_id)
# return render(request, 'quiz/results.html', {'question': question})


# @login_required
# def response_view(request):
#     if request.method == 'POST':
#         form = ResponseForm(request.POST)
#         if form.is_valid():
#             form = form.save(commit=False)
#             form.user = request.user
#             form.save()
#             return redirect('/')
#     else:
#         form = ResponseForm()
#     return render(request, 'quiz/response.html', {'form': form})


# def answer(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = MyForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             return HttpResponseRedirect('/quiz/')

#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = MyForm()

#     return render(request, '/quiz/quiz.html', {'form': form})


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
#        
# )

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