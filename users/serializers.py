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


# ДЗ
# ПРОПИСАТЬ serializers ДЛЯ UserCardModel и TransferModel
# ПРОПИСАТЬ views для новых serializers
# ПРОПИСАТЬ путь(urls) для новых views

