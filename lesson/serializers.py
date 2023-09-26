from rest_framework import serializers

from lesson.models import Lesson, LessonStatus


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = ['id', 'lesson_name', 'lesson_duration', 'video_link']


class LessonStatusSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer(read_only=True)

    class Meta:
        model = LessonStatus
        fields = ['lesson', 'lesson_status', 'lesson_watch_duration']


class LessonLastWatchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = ['id', 'lesson_name', 'lesson_duration', 'video_link']


class LessonStatusLastWatchSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer(read_only=True)

    class Meta:
        model = LessonStatus
        fields = ['lesson', 'lesson_status', 'lesson_watch_duration', 'last_time_watched']
