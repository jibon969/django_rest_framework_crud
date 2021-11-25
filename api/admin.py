from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_per_page = 0
    search_fields = ['title']
    list_display = ['title']

    class Meta:
        model = Task
