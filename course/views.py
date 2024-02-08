from django.shortcuts import render, get_object_or_404
from course.models import Category, Course
# Create your views here.

def categories_view(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'category/category-home.html', context)

def category_single(request, pid):
    courses = get_object_or_404(Category,pk=pid).course_set.all()
    category = get_object_or_404(Category,pk=pid)
    context = {'courses': courses, 'category_pid': pid, 'category': category}
    return render(request, 'category/category-single.html', context)

def course_view(request, category_id, course_id):
    course = get_object_or_404(Course,pk=course_id)
    context = {'course': course}
    return render(request, 'course/course.html', context)