from rest_framework.response import Response
from courses.models import Course,Lessons,Videos
from account.models import User
from.serializers import CourseSerializers,LessonsSerializers,VideosSerializers,UserSerializers
from rest_framework import generics,status


class CourseListCreateApiView(generics.ListCreateAPIView):
    queryset=Course.objects.all()
    serializer_class=CourseSerializers

class CoursedetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Course.objects.all()
    serializer_class=CourseSerializers



class LessonsListCreateApiView(generics.ListCreateAPIView):
    queryset=Lessons.objects.all()
    serializer_class=LessonsSerializers

class LessonsdetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Lessons.objects.all()
    serializer_class=LessonsSerializers



class VideosListCreateApiView(generics.ListCreateAPIView):
    queryset=Videos.objects.all()
    serializer_class=VideosSerializers

class VideosdetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Videos.objects.all()
    serializer_class=VideosSerializers



class UserListCreateApiView(generics.ListCreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializers

class UserdetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializers


    