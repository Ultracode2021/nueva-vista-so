from django.contrib import admin
from .models import Question

@admin.register(Question)

class QuestionAdmin(admin.ModelAdmin):
    fields = ('text', 'choice_text', 'date')
    list_display = ('id', 'text', 'choice_text', 'date')