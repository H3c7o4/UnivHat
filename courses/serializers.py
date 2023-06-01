from rest_framework import serializers

from courses.models import Evaluation, Course, Classroom
from accounts.serializers import Userserializers


class CourseSerializer(serializers.ModelSerializer):
    students = Userserializers(many=True, read_only=True)
    class Meta:
        model = Course
        fields = '__all__'
        extra_kwargs = {'students': {'required': False}}

class EvaluationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Evaluation
        fields = '__all__'

class ClassroomSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True, read_only=True)
    students = Userserializers(many=True, read_only=True)

    class Meta:
        model = Classroom
        fields = '__all__'
        extra_kwargs = {'courses': {'required': False}}