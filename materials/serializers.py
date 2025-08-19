from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from materials.models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lessons = LessonSerializer()

    class Meta:
        model = Course
        fields = '__all__'

    def get_lesson_count(self, instance):
        if instance.lesson_set.all():
            return len(instance.lesson_set.all())
        return 0