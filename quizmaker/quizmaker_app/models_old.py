import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

	#....
	def __str__(self):
		return self.question_text

	#....
	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class CorrectAnswer(models.Model):
	correct_answer_text = models.CharField(max_length=200)

	question = models.OneToOneField(Question, on_delete=models.CASCADE)

	#....
	def __str__(self):
		return self.correct_answer_text


class WrongAnswer(models.Model):
	potential_answer_text = models.CharField(max_length=200)

	question = models.ForeignKey(Question, on_delete=models.CASCADE)

	#....
	def __str__(self):
		return self.potential_answer_text



