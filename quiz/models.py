from django.db import models
from django.contrib.auth.models import AbstractUser

# Topic model choices
class Topic(models.TextChoices):
    AI = "AI"
    CYBER_SECURITY = "Cyber Security"
    BACKEND = "Backend"
    MOBILE = "Mobile"

class Question(models.Model):
    question_text = models.CharField(max_length=500)
    topic = models.CharField(max_length=50, choices=Topic.choices)
    correct_answer_index = models.IntegerField(choices=[(0, 'Option 1'), (1, 'Option 2'), (2, 'Option 3'), (3, 'Option 4')])  # 0-3 options
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)

    def __str__(self):
        return self.question_text[:50]

    @property
    def options(self):
        return [self.option1, self.option2, self.option3, self.option4]

    class Meta:
        db_table = 'questions'
