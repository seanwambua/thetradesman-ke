from rest_framework import serializers
from apps.accounts.models import CustomUser
from apps.store.models import Products


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"