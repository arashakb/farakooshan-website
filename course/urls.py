from django.urls import path
from course.views import *

app_name = 'course'

urlpatterns = [
    path('<int:category_id>/course/<int:course_id>', course_view, name="course-single"),
    path('<int:pid>', category_single, name="single"),
    path('', categories_view, name="categories"),

]