from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Receipt, Item
from .serializers import ReceiptSerializer, ItemSerializer

@api_view(['GET'])
def getReceiptPoints(request, receiptId):
    try:
        receipt = Receipt.objects.get(receiptId = receiptId)
    except Reciept.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    serializer = ReceiptSerializer(receipt)
    Response(serializer.data)

@api_view(['POST'])
def processReceipt(request):
    serializer = ReceiptSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
