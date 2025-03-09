from django.contrib import admin
from .models import Question

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'topic', 'correct_answer_index')
    list_filter = ('topic',)
    search_fields = ('question_text', 'topic')

admin.site.register(Question, QuestionAdmin)
