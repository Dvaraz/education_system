from django.contrib import admin

from lesson.models import Lesson, LessonStatus, ProductLesson

admin.site.register(Lesson)
admin.site.register(LessonStatus)
admin.site.register(ProductLesson)
