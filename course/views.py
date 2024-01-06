from django.shortcuts import render, get_object_or_404
from course.models import Category
# Create your views here.

def categories_view(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'category/category-home.html', context)

def category_single(request, pid):
    courses = get_object_or_404(Category,pk=pid).course_set.all()
    context = {'courses': courses, 'category_pid': pid}
    return render(request, 'category/category-single.html', context)

def course_view(request, category_id, course_id):
    return render(request, 'course/course.html')