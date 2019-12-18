from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.template import loader

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)
    # template = loader.get_template('polls/index.html')
    # return HttpResponse(template.render(context, request))


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('Question does not exist!')

    context = {
        'question': question,
    }
    return render(request, 'polls/detail.html', context)


def results(request, question_id):
    response = "You're looking at the results of question {}"
    return HttpResponse(response.format(question_id))


def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}.")