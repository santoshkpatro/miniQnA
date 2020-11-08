from django.db.models.manager import EmptyManager
from django.shortcuts import redirect, render
from django.utils import timezone

from .models import Question, Answer

# Create your views here.
def main_view(request):
    if request.POST:
        new_question = Question(question_text=request.POST.get('question'), pub_date=timezone.now())
        new_question.save()

    question_list = Question.objects.all()
    context = {
        'question_list': question_list
    }

    return render(request, 'main_view.html', context)


def qn_add_view(request):
    if request.POST:
        new_question = Question(question_text=request.POST.get('question'))
        new_question.save()
    
    return redirect(main_view)


def ans_add_view(request, qn_id):
    if request.POST:
        q = Question.objects.get(pk=qn_id)
        new_answer = Answer(question=q, answer_text=request.POST.get('answer'), votes=2)
        new_answer.save()

    return redirect(main_view)


def ans_vote_view(request, ans_id):
    if request.POST:
        ans = Answer.objects.get(pk=ans_id)
        ans.votes = ans.votes + 1
        ans.save()

    return redirect(main_view)