from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.template import loader

from .models import Quiz

unviewed_results = False

# Create your views here.

def index(request):
	template = loader.get_template('quizmaker_app/index.html')
	context = {
		'unviewed_results': unviewed_results
	}
	return HttpResponse(template.render(context, request))

def makeQuiz(request):
	return HttpResponse("You want to make a quiz!")

def takeQuiz(request, quiz_id):
	response = "You want to take a quiz you made! Quiz %s"
	try :
		quiz = Quiz.objects.get(pk=quiz_id)
	except Quiz.DoesNotExist:
		raise Http404("Quiz does not exist")

	unviewed_results = True
	context = {'quiz_id' : quiz_id}
	return render(request, 'quizmaker_app/takequiz.html', context)

def takingQuiz(request, quiz_id):
	try :
		quiz = Quiz.objects.get(pk=quiz_id)
	except Quiz.DoesNotExist:
		raise Http404("Internal error....")

	context = {'quiz_id' : quiz_id, 'quiz' : quiz}

	return render(request, 'quizmaker_app/takequiz_go.html', context)


def viewQuizResults(request, quiz_id):
	response = "You want to see your results after taking a quiz! Quiz %s"
	return HttpResponse(response % quiz_id)

def viewMadeQuiz(request, quiz_id):
	response = "You want to view a quiz you made! Quiz %s"
	return HttpResponse(response % quiz_id)





