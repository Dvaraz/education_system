from rest_framework.response import Response
from rest_framework.views import APIView

from django.contrib.auth.models import User
from lesson.models import LessonStatus, ProductLesson
from lesson.serializers import LessonStatusSerializer
from product.models import Access


class LessonView(APIView):
    def get(self, request):
        user = self.request.user.id
        user = User.objects.filter(id=user).first()

        product_list = []
        lesson_list = []

        products_has_access = Access.objects.filter(user=user, access=True)

        for product in products_has_access:
            product_list.append(product.product_id)
        lessons = ProductLesson.objects.filter(product_id__in=list(product_list))
        for lesson in lessons:
            lesson_list.append(lesson.lesson_id)

        lessons_with_status = LessonStatus.objects.filter(lesson_id__in=list(lesson_list), user=user).select_related('lesson')

        lesson_serializer = LessonStatusSerializer(lessons_with_status, many=True)

        return Response(lesson_serializer.data)

