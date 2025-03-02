from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    job_limit = models.IntegerField(default=5)

    def __str__(self):
        return self.user.username
    

class Job(models.Model):
 
    job_name = models.CharField(max_length=100)

    description = models.TextField()

    skills_required = models.CharField(max_length=200)

    experience_required = models.CharField(max_length=100)

    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.job_name