from django.urls import path
from course.views import *

app_name = 'course'

urlpatterns = [
    path('courses', course_view, name="index"),
    path('<int:pid>', category_single, name="single"),
    path('', categories_view, name="categories"),

]