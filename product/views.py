from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Sum

from django.contrib.auth.models import User
from lesson.models import LessonStatus, ProductLesson
from lesson.serializers import LessonStatusLastWatchSerializer
from product.models import Product, Access


class ProductStatisticView(APIView):

    def get(self, request):

        data_dict = {}

        products = Product.objects.all()

        for product in products:
            lessons = ProductLesson.objects.filter(product_id=product.id)

            access = Access.objects.filter(product_id=product.id, access=True)
            lessons_on_product = [lesson.lesson_id for lesson in lessons]
            users_on_product = [user.user_id for user in access]

            spent_time_total = LessonStatus.objects.filter(lesson__in=list(lessons_on_product), user__in=list(users_on_product)).aggregate(total=Sum('lesson_watch_duration'))

            total_users = User.objects.all().count()
            buy_percent = f'{len(access) / total_users:.2%}'

            product_information = {product.product_name: {
                'lessons_watched_total': len(lessons),
                'spent_time_total': spent_time_total['total'],
                'number_of_students': len(access),
                'buy_percent': buy_percent,

            }}
            data_dict.update(product_information)
        return Response(data_dict)


class ProductLessonsView(APIView):

    def get(self, request, product):
        user = self.request.user.id
        user = User.objects.filter(id=user).first()

        lesson_list = []

        product_has_access = Access.objects.filter(user=user, product__product_name=product, access=True).select_related('product').first()
        if product_has_access:
            lessons = ProductLesson.objects.filter(product_id=product_has_access.product)

            for lesson in lessons:
                lesson_list.append(lesson.lesson_id)

            lessons_with_status = LessonStatus.objects.filter(lesson_id__in=list(lesson_list), user=user).select_related('lesson')

            lesson_serializer = LessonStatusLastWatchSerializer(lessons_with_status, many=True)

            return Response(lesson_serializer.data)
        else:
            return Response({
                        'response': 'Sorry you do not have this product yet, but you always can buy it!!! SUPER SALE NOW!!!!'
                    })
