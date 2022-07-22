from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField(default=0)
    rating = models.PositiveIntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="courses")
    students = models.ManyToManyField(User)
    update_date = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.title

    


class Lessons(models.Model):
    lessons_name=models.CharField(max_length=100)
    lessons_title=models.ForeignKey(Course,on_delete=models.CASCADE, related_name="lessons")
    
    def __str__(self) -> str:
        return self.lessons_name



class Videos(models.Model):
    videos=models.FileField(null=True,blank=True)
    video_name=models.CharField(max_length=100)
    videos_title=models.ForeignKey(Lessons,on_delete=models.CASCADE, related_name="videos")

    def __str__(self) -> str:
        return self.video_name
    



