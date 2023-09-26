from rest_framework import serializers

from lesson.models import Lesson, LessonStatus
from product.models import Product
from account.serializers import UserSerializer
from lesson.serializers import LessonStatusLastWatchSerializer, LessonSerializer


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product

        fields = ['id', 'product_name']



