from django.shortcuts import render
from django.http import HttpResponse
from course.models import Category
from django.utils.translation import activate
# Create your views here.

def home_view(request):
    categories = Category.objects.all()
    context = {"categories": categories}
    activate('en')
    return render(request, 'website/index.html', context)

def about_view(request):
    return render(request, 'website/about.html')

def contact_view(request):
    return render(request, 'website/contact.html')