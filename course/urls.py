from django.urls import path
from course.views import *

app_name = 'course'

urlpatterns = [
    path('', course_view, name="index"),
    path('single', course_single, name="single"),
    

]