from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    priority_choices = (
        (1, 'Low'),
        (2, 'Medium'),
        (3, 'High'),
    )
    priority = models.IntegerField(choices=priority_choices)
    def __str__(self):
        return self.name

class Ticket(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=200)
    status_choices = (
        ('OPEN', 'Open'),
        ('IN_PROGRESS', 'In Progress'),
        ('CLOSED', 'Closed'),
    )
    status = models.CharField(max_length=20, choices=status_choices)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} - {self.description[:50]} - {self.created_at} - {self.author} - {self.status}"
