from django.urls import path

# from lesson.views import LessonViewSet
from product.views import ProductLessonsView, ProductStatisticView


urlpatterns = [
    path('statistic', ProductStatisticView.as_view(), name='product_statistic'),
    path('<str:product>', ProductLessonsView.as_view(), name='product_lessons'),
]