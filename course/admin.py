from django.contrib import admin
from course.models import Course, Category
# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title', 'price', 'status', 'start_date', 'created_date')
    list_filter = ['status']
    ordering = ['-created_date']
    search_fields = ['title', 'content', 'objectives', 'description']

admin.site.register(Course, CourseAdmin)
admin.site.register(Category)
