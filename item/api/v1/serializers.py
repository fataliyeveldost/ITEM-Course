from rest_framework import serializers
from courses.models import Course,Lessons,Videos
from account.models import User



class  CourseSerializers(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields="__all__"

class LessonsSerializers(serializers.ModelSerializer):
    class Meta:
        model=Lessons
        fields="__all__"

class VideosSerializers(serializers.ModelSerializer):
    class Meta:
        model=Videos
        fields="__all__"

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields="__all__"
