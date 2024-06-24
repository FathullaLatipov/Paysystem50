# serializers.py
from rest_framework import serializers

from users.models import UserModel, UserCardModel, TransferModel


# serializer for user
class UserModelSerializer(serializers.ModelSerializer):
    # username = serializers.CharField()
    class Meta:
        model = UserModel
        # fields = ['name', 'asdf', 'adsf'] перечисления нужных значений
        fields = '__all__' # получить все колонки(значения)
        # exclude = ['id'] исключить


class UserCardModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserCardModel
        fields = '__all__'


class TransferModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = TransferModel
        fields = '__all__'

# ДЗ
# ПРОПИСАТЬ serializers ДЛЯ UserCardModel и TransferModel
# ПРОПИСАТЬ views для новых serializers
# ПРОПИСАТЬ путь(urls) для новых views

