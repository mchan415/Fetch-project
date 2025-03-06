from django.db import models
import uuid

# This is used to act as our database to store the data after we receive the input
class Receipt(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    retailer = models.CharField(max_length = 255)
    purchaseDate = models.DateField()
    purchaseTime = models.TimeField()
    total = models.DecimalField(max_digits = 10, decimal_places = 2)
    points = models.IntegerField(default = 0)

class Item(models.Model):
    receipt = models.ForeignKey(Receipt, on_delete = models.CASCADE, related_name = "items")
    shortDescription = models.CharField(max_length = 255)
    price = models.DecimalField(max_digits = 10, decimal_places = 2)


    


    