from django.db import models

from django.utils.html import format_html

class Task(models.Model):
    # nom
    name = models.CharField(max_length=50)
    # description
    description = models.TextField()
    # date de création
    created_date = models.DateField(auto_now_add=True)
    # date de contraite
    due_date = models.DateField(auto_now_add=True)
    # closed
    closed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
    def colored_due_date(self):
        color = 'red'
        return format_html(f'<span style="color:{color}">{self.due_date}</span>')