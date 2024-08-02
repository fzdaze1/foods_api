from rest_framework import generics
from rest_framework.response import Response
from .models import FoodCategory
from .serializers import FoodListSerializer


class FoodCategoryListView(generics.ListAPIView):
    serializer_class = FoodListSerializer

    def get_queryset(self):
        return FoodCategory.objects.filter(food__is_publish=True).distinct().order_by('id')

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
