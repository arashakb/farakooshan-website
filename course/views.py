from django.shortcuts import render, get_object_or_404
from course.models import Category
# Create your views here.

def categories_view(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'category/category-home.html', context)

def course_view(request):
    return render(request, 'course/categories.html')

def category_single(request, pid):
    courses = get_object_or_404(Category,pk=pid).course_set.all()
    context = {'courses': courses}
    return render(request, 'category/category-single.html', context)