from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.name

class TodoList(models.Model):
    title = models.CharField(max_length=300)
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    dueDate = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    completed = models.BooleanField(default=False)
    important = models.BooleanField(default=False)
    category = models.ForeignKey(Category, default="General", on_delete=models.CASCADE)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.title