from django.db import models
from django.contrib.auth.models import User

class Projects(models.Model):
    TIER_CHOICES = [
        ('Free', 'Free'),
        ('Premium', 'Premium'),
    ]
    
    DIFFICULTY_CHOICES = [
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
    ]
    project_key = models.CharField(max_length=50, unique=True, null=True, blank=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    tier = models.CharField(max_length=10, choices=TIER_CHOICES)
    difficulty_level = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES, default='Beginner')
    requirements = models.TextField(blank=True)
    is_featured = models.BooleanField(default=False)
    resources = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    estimated_time = models.CharField(max_length=50, blank=True)
    

    def __str__(self):
        return self.name
