import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Quiz(models.Model):
	quiz_id = models.IntegerField(unique=True);

	#....
	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

	#....
	def __str__(self):
		return "Quiz #" + str(self.quiz_id)


class Question(models.Model):
	question_text = models.CharField(max_length=200)
	
	quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

	#....
	def __str__(self):
		return self.question_text


class Answer(models.Model):
	answer_text = models.CharField(max_length=200)
	is_correct = models.BooleanField()

	question = models.ForeignKey(Question, on_delete=models.CASCADE)

	#....
	def __str__(self):
		tail_str = ""
		if (self.is_correct):
			tail_str = " (correct)"
		return self.answer_text + str(tail_str)
