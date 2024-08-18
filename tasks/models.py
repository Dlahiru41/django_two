from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Task(models.Model):
    user_email = models.EmailField()
    task = models.CharField(max_length=200)
    due_by = models.DateTimeField()
    priority = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(3)]
    )
    is_urgent = models.BooleanField(default=False)

    def __str__(self):
        return self.task