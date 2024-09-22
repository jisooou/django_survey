from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from .models import Question

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    context = {'latest_question_list':latest_question_list}

    return render(request, 'polls/index.html', context)


def detail(request, question_id):

    q = get_object_or_404(Question, pk=question_id)

    # try:
    #     q = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404('Question {} does not exit'.format(question_id))

    return render(request, 'polls/detail.html', {'question':q})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    try:
        seleted_choice = question.choice_set.get(id=request.POST['choice_select'])
        # question.choice_set.get(id=7)
        # Choice.objects.get(id=99)
    except: 
        context = {'question':question, 'error_message':"You didn't select a choice."}
        return render(request, 'polls/detail.html', context)
    else:
        seleted_choice.votes += 1
        seleted_choice.save()
        return redirect('polls:results', question_id=question.id)

    # request.POST['choice_select'] 

def results(request, question_id):
    question = get_object_or_404(Question, id=question_id)

    return render(request, 'polls/result.html', {'question': question})
