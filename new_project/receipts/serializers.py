from rest_framework import serializers
from .models import Receipt, Item


# This is used to convert model into json data that we can access from our api
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ["shortDescription", "price"]

class ReceiptSerializer(serializers.ModelSerializer):
    purchaseTime = serializers.TimeField(format = "%H:%M", input_formats = ["%H:%M", "%H:%M:%S"])
    items = ItemSerializer(many = True)
    

    class Meta:
        model = Receipt
        fields = "__all__"
        read_only_fields = ["points"]

    def create(self, validated_data):
        items_data = validated_data.pop("items")
        receipt = Receipt.objects.create(**validated_data)
        for item_data in items_data:
            Item.objects.create(receipt = receipt, **item_data)

        return receipt