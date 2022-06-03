from django.contrib import admin

from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'closed', 'created_date', 'colored_due_date']
    list_filter = ['closed', 'created_date', 'due_date']
    search_fields = ['name__startswith']
    date_hierarchy = 'due_date'

admin.site.register(Task, TaskAdmin)