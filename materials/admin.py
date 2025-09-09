from django.contrib import admin
from materials.models import Course, Lesson, Subscription


# Register your models here.
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    exclude = ()

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    exclude = ()

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    exclude = ()
