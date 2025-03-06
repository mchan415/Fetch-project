from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Receipt, Item
from .serializers import ReceiptSerializer, ItemSerializer
from .services.pointsCalculation import calculatePoints


@api_view(['GET'])
def getReceiptPoints(request, receiptId):
    try:
        receipt = Receipt.objects.get(id = receiptId)
    except Receipt.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    serializer = ReceiptSerializer(receipt)
    return Response({"points": serializer.data["points"]})

@api_view(['POST'])
def processReceipt(request):
    serializer = ReceiptSerializer(data = request.data)
    if serializer.is_valid():
        serializer.validated_data["points"] = calculatePoints(serializer)
        serializer.save()
        return Response({"id": serializer.data["points"]}, status = status.HTTP_201_CREATED)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
