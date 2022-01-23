from django import forms

class AnswerForm(forms.Form):
    answer = forms.CharField(max_length=100)
   


    # you have your questions written out on the page
    #################################################
    # for each question in question model where quix = x {
    #   display question.name = show
    #       
    #       for each choice in thhat question {
    #           display choice.name = show
    #   }

    # }



    # now you can display all choices for each question on a page
    # 
    # need a way to take choice use it as an input for choice_answer
    # then store that choice in quizAnswer model for each question

    # finally take all quizAnswers then process them