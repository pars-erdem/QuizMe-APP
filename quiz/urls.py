from . import views
from django.urls import path


urlpatterns = [
    # Template URLs
    path('', views.index, name='index'),
    path('quiz/ai/', views.ai_quiz, name='ai_quiz'),
    path('quiz/cyber/', views.cyber_quiz, name='cyber_quiz'),
    path('quiz/backend/', views.backend_quiz, name='backend_quiz'),
    path('quiz/mobile/', views.mobile_quiz, name='mobile_quiz'),
]