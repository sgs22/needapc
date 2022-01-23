from django.shortcuts import render

from .forms import AnswerForm

def get_answer(request):
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            return  HttpResponseRedirect('/thanks/')
    else:
        form = AnswerForm()
    return render(request, 'answer.html', {'form': form})
