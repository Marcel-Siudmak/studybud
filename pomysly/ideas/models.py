from django.db import models

# Create your models here.

IDEA_STATUS = (
    ('pending', 'waiting for review'),
    ('accepted', 'Accepted'),
    ('done', 'Done'),
    ('rejected', 'Rejected')
)

class Idea(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    youtube = models.URLField()
    status = models.CharField(choices=IDEA_STATUS, max_length=35, default='pending')

class Votes(models.Model):
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE)
    reason = models.TextField()