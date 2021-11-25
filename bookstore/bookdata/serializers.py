from rest_framework import serializers


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'bookname', 'amount', 'pic_url', 'price']