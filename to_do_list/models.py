from django.db import models

# Create your models here.
class Task(models.Model):
    id=models.TextField(primary_key=True)
    title=models.TextField(max_length=200)
    completed=models.BooleanField(default=False,blank=True,null=True)

    def __str__(self):
        return self.title