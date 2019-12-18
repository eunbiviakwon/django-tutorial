from django.contrib import admin
from .models import Question, Choice


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    pass
# Register your models here.
