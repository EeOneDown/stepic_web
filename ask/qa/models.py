from django.db import models
from django.contrib.auth.models import User


class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-added_at')
    def popular(self):
        return self.order_by('-rating')


class Question(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField()
    added_at = models.DateField(blank=True, auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(
        User, related_name='q_to_u', on_delete=models.CASCADE
    )
    likes = models.ManyToManyField(User, related_name='q_to_l')

    objects = QuestionManager()


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField()
    question = models.ForeignKey(
        Question, related_name='a_to_q', on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        User, related_name='a_to_u', on_delete=models.CASCADE
    )
