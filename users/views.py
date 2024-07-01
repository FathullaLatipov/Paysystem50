from django.shortcuts import render
from rest_framework import generics
from users.models import UserModel, UserCardModel, TransferModel
from users.serializers import UserModelSerializer, UserCardModelSerializer, TransferModelSerializer

from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework.pagination import PageNumberPagination
# from rest_framework.pagination import LimitOffsetPagination


# переход через страницы и через числа
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 2  #кол-во товаров на одном странице
    max_page_size = 1000  # 1000


@api_view()
def hello_world(request):
    return Response({"message": "Hello, world!"})


class TestAPIView(APIView):

    def get(self, request):
        users = UserModel.objects.all()  #user1, user2, user3
        user_serializers = UserModelSerializer(users, many=True)
        return Response(user_serializers.data)

    def post(self, request, format=None):
        serializer = UserModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserModelListAPIView(generics.ListAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name', 'email']
    permission_classes = [permissions.AllowAny]
    pagination_class = StandardResultsSetPagination
    filterset_fields = ['name', 'phone_number']


class UserModelCreateAPIView(generics.CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer


class UserModelUpdateAPIView(generics.UpdateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        pass


class UserModelRetrieveAPIView(generics.RetrieveAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer


class UserModelDestroyAPIView(generics.DestroyAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer


class UserCartListAPIView(generics.ListAPIView):
    queryset = UserCardModel.objects.all()
    serializer_class = UserCardModelSerializer


class UserCartCreateAPIView(generics.CreateAPIView):
    queryset = UserCardModel.objects.all()
    serializer_class = UserCardModelSerializer


class UserCartUpdateAPIView(generics.UpdateAPIView):
    queryset = UserCardModel.objects.all()
    serializer_class = UserCardModelSerializer


class UserCartRetrieveAPIView(generics.RetrieveAPIView):
    queryset = UserCardModel.objects.all()
    serializer_class = UserCardModelSerializer


class UserCartDestroyAPIView(generics.DestroyAPIView):
    queryset = UserCardModel.objects.all()
    serializer_class = UserCardModelSerializer


class TransferModelListAPIView(generics.ListAPIView):
    queryset = TransferModel.objects.all()
    serializer_class = TransferModelSerializer


class TransferModelCreateAPIView(generics.CreateAPIView):
    queryset = TransferModel.objects.all()
    serializer_class = TransferModelSerializer


class TransferModelUpdateAPIView(generics.UpdateAPIView):
    queryset = TransferModel.objects.all()
    serializer_class = TransferModelSerializer


class TransferModelRetrieveAPIView(generics.RetrieveAPIView):
    queryset = TransferModel.objects.all()
    serializer_class = TransferModelSerializer


class TransferModelDestroyAPIView(generics.DestroyAPIView):
    queryset = TransferModel.objects.all()
    serializer_class = TransferModelSerializer


class Home(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)