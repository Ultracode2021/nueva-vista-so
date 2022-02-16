from django.db import models

class Question (models.Model):
    text = models.CharField(max_length=55)
    choice_text = models.CharField(max_length=33)
    date = models.DateField()

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=33)
    votes = models.IntegerField(default=0)