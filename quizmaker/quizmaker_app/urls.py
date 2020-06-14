from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('createquiz', views.makeQuiz),
    path('takequiz/<int:quiz_id>/', views.takeQuiz),
    path('viewresults/<int:quiz_id>/', views.viewQuizResults),
    path('viewquiz/<int:quiz_id>/', views.viewMadeQuiz),
    path('takequiz/<int:quiz_id>/go/', views.takingQuiz)
]

