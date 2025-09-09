from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from materials.models import Course, Lesson, Subscription
from materials.validators import LinkValidator


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [LinkValidator(field='link'), ]


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField(read_only=True)
    lessons = LessonSerializer()
    subscription = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Course
        fields = '__all__'

    def get_lesson_count(self, instance):
        return instance.lesson_set.count()

    def get_subscription(self, obj):
        request = self.context.get('request')
        user = request.user
        return Subscription.objects.all().filter(user=user).filter(course=obj).exists()


class SubSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = '__all__'