from django.shortcuts import render
from django.shortcuts import redirect

from .models import Question, AnswerChoice


def create_question_object(post):
    submission = Question()
    if post['question_body'] == '':
        submission.delete()
        return
    if post['source_year'] == '':
        submission.delete()
        return
    if post['source_event'] == '':
        submission.delete()
        return
    if all([post['choice_{}'.format(letter)] == '' for letter in 'abcde']):
        submission.delete()
        return
    submission.question_body = post['question_body']
    submission.source_event = post['source_event']
    submission.source_year = int(post['source_year'])
    submission.solution_latex = ''
    submission.accepted_answer = ''
    submission.context = ''

    for letter in 'abcde':
        answer_latex = post['choice_{}'.format(letter)]
        if answer_latex == '':
            continue
        choice = AnswerChoice()
        choice.question = submission
        choice.letter = letter
        choice.latex = answer_latex
        choice.save()

    submission.save()


def add_question(request):
    if request.method == "GET":
        return render(request, 'testgen/index.html')
    elif request.method == "POST":
        return render(request, 'testgen/index.html')


def submit_question(request):
    if request.method == "POST":
        submission = Question()
        submission.question_body = request.POST['question_body']
    return redirect('/')
