from django.shortcuts import render
from course.models import Category
# Create your views here.

def categories_view(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'category/category-home.html', context)

def course_view(request):
    return render(request, 'course/categories.html')

def course_single(request, pid):
    return render(request, 'category/category-single.html')