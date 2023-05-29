
from accounts.models import CustomUser
from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=25)
    description = models.CharField(max_length=255)
    video = models.FileField(upload_to='public_video_course', null=True, blank=True)
    textfile = models.FileField(upload_to='public_files', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    students = models.ManyToManyField(CustomUser)

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self):
        return self.title


class Evaluation(models.Model):
    title = models.CharField(max_length=25)
    description = models.CharField(max_length=255)
    textfile = models.FileField(upload_to='evaluations_files', null=True, blank=True)
    due_date = models.DateField(auto_now_add=False)
    completed = models.BooleanField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    course = models.ForeignKey('Course', null=False, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Evaluation'
        verbose_name_plural = 'Evaluations'

    def __str__(self):
        return self.title


class Classroom(models.Model):
    name = models.CharField(max_length=255)
    courses = models.ManyToManyField(Course)
    students = models.ManyToManyField(CustomUser)

    class Meta:
        verbose_name = 'Classroom'
        verbose_name_plural = 'Classrooms'

    def __str__(self):
        return self.name