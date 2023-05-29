from django.contrib import admin
from courses.models import Course, Evaluation, Classroom

# Register your models here.
class CourseInLine(admin.TabularInline):
    model = Evaluation
    extra = 0

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'textfile')
    inlines = (CourseInLine, )
    search_fields = ('title', 'description')

@admin.register(Evaluation)
class EvaluationAdmin(admin.ModelAdmin):
    list_display = ('title', 'completed', 'due_date')
    list_filter = ('completed', 'due_date')

@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    list_display = ('name', )