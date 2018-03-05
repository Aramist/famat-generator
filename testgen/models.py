from django.db import models


class Context(models.Model):
    latex = models.CharField(max_length=500)


class Question(models.Model):
    source_event = models.IntegerField()
    source_year = models.IntegerField()
    date_added = models.DateTimeField(auto_now=True)
    question_body = models.CharField(max_length=500)
    solution_latex = models.CharField(max_length=500)
    accepted_answer = models.CharField(max_length=10)
    context = models.ForeignKey(Context, blank=True, null=True, on_delete=models.CASCADE)


class AnswerChoice(models.Model):
    latex = models.CharField(max_length=100)
    letter = models.CharField(max_length=1)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)


class Category(models.Model):
    name = models.CharField(max_length=20)
    supercategory = models.CharField(max_length=20)
    bitmask_power = models.IntegerField()
