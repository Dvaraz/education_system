import uuid

from django.db import models
from django.contrib.auth.models import User
from product.models import Product


class Lesson(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    lesson_name = models.CharField(max_length=120, null=False)
    video_link = models.URLField(max_length=200, null=True, blank=True)
    lesson_duration = models.IntegerField(null=False)
    user = models.ManyToManyField(User, through='LessonStatus')
    lesson = models.ManyToManyField(Product, through='ProductLesson')

    def __str__(self):
        return self.lesson_name


class LessonStatus(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='status_lesson')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_lesson_status')
    lesson_watch_duration = models.IntegerField(blank=True, null=True)
    lesson_status = models.BooleanField(default=False)
    last_time_watched = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.lesson.lesson_name}, {self.user.username}'


class ProductLesson(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_lesson_product')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='product_lesson_lesson')

    def __str__(self):
        return f'{self.product.product_name}, {self.lesson.lesson_name}'
