from django import views
from django.urls import path
from.import views

urlpatterns = [
    path('', views.CourseListCreateApiView.as_view()),
    

    path('course', views.CourseListCreateApiView.as_view()),
    path('course/<int:pk>', views.CoursedetailApiView.as_view()),

    path('Lessons', views.LessonsListCreateApiView.as_view()),
    path('Lessons/<int:pk>', views.LessonsdetailApiView.as_view()),

    path('Videos', views.VideosListCreateApiView.as_view()),
    path('Videos/<int:pk>', views.VideosdetailApiView.as_view()),

    path('User', views.UserListCreateApiView.as_view()),
    path('User/<int:pk>', views.UserdetailApiView.as_view()),

]