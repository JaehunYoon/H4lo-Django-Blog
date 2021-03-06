from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.template import loader
from django.http import HttpResponse
from .models import Question


def detail(request, question_id):
    return HttpResponse(f"You're looking at question {question_id}")


def results(self, question_id):
    res = "You're looking at the results of question %s"
    return HttpResponse(res % question_id)


def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}.")


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')

    context = {'latest_question_list': latest_question_list}
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)
