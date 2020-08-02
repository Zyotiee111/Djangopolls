from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse

from .models import Question, Choices


# Create your views here.
def index(request):
    questions = Question.objects.order_by('-pub_date')[:5]
    context = {'questions': questions, }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):

    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('Question does not exist')
    context = {
        "question": question,

    }
    return render(request, 'polls/detail.html', context)


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def votes(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choices_set.get(pk= request.POST['choice'])
    except:
        return render(request, 'polls/detail.html',  {
            'question': question, 'error_message': "please select a choice",
        })
    else:
        selected_choice.votes +=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))



