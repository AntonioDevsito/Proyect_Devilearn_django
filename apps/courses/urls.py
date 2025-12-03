from django.urls import path
from . import views
urlpatterns = [
    path('',views.course_list ,name="course_list" ),#/courses/
    path('detail',views.course_detail ,name="course_detail" ),#/courses/
    path('lessons',views.course_lessons ,name="course_lessons" ),#/courses/
    path('profile',views.profile ,name="course_profile" ),#/courses/
    path('index', views.index, name="course_index"),
]

