from django.shortcuts import render

# Create your views here.
def category_view(request):
    return render(request, 'category/category-home.html')
def category_single(request):
    pass