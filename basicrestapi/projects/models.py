from django.db import models
from django.conf import settings

class Project(models.Model):
    title = models.CharField(max_length=30)
    description = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='project_assigned_by',
        null = True
    )
    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='project_assigned_to',
        null = True
    )

    start_date = models.DateTimeField(auto_now_add=False)
    end_date = models.DateTimeField(auto_now_add =False, null=True)

    def __str__(self):
        return self.title