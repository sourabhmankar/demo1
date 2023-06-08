from django.db import models
class student(models.Model):
    rollno=models.IntegerField()
    name=models.CharField(max_length=30)
    email=models.EmailField()
    class Meta:
        db_table="Student"
# Create your models here.
