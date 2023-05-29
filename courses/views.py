from django.shortcuts import render
from rest_framework import viewsets
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response

from courses.models import Evaluation, Course, Classroom
from courses.serializers import EvaluationSerializer, CourseSerializer, ClassroomSerializer


# Create your views here.
class Courseviewset(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class Evaluationviewset(viewsets.ModelViewSet):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer

class Classroommviewset(viewsets.ModelViewSet):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer