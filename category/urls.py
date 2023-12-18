from django.urls import path
from category.views import *

app_name = 'category'

urlpatterns = [
    path('', category_view, name="index"),
    path('single', category_single, name="single"),
    

]