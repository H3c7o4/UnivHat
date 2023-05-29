from rest_framework import serializers

from courses.models import Evaluation, Course, Classroom
from accounts.serializers import Userserializers


class CourseSerializer(serializers.ModelSerializer):
    students = Userserializers(many=True)
    class Meta:
        model = Course
        fields = '__all__'

class EvaluationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Evaluation
        fields = '__all__'

class ClassroomSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True)
    students = Userserializers(many=True)

    class Meta:
        model = Classroom
        fields = '__all__'