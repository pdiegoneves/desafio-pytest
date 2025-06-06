from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        symbol = "✅" if self.completed else "❌"
        return f"{symbol} -> {self.title}"
