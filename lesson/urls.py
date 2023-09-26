from django.urls import path

# from lesson.views import LessonViewSet
from lesson.views import LessonView


urlpatterns = [
    path('lessonsList', LessonView.as_view(), name='lessons_list'),
]
