from django.db import models


class UserModel(models.Model):
    name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=80)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    country = models.CharField(max_length=90)
    password = models.CharField(max_length=120)
    updated_at = models.DateTimeField(auto_now=True) # 17:54
    created_at = models.DateTimeField(auto_now_add=True) # 17:50

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class UserCardModel(models.Model):
    card_name = models.CharField(max_length=130)
    card_number = models.IntegerField()
    balance = models.FloatField(default=0)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    exp_date = models.IntegerField()

    def __str__(self):
        return self.card_name

    class Meta:
        verbose_name = 'User card'
        verbose_name_plural = 'User cards'


class TransferModel(models.Model):
    card_from = models.ForeignKey(UserCardModel, related_name='transfers_from', on_delete=models.CASCADE)
    card_to = models.ForeignKey(UserCardModel, related_name='transfers_to', on_delete=models.CASCADE)
    amount = models.FloatField(default=0)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = 'Transfer'
        verbose_name_plural = 'Transfers'