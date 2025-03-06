from datetime import datetime
from .stringUtils import alnumPoints

def pointsFromTotal(total):
    points = 0
    total = float(total)
    if total % 1 == 0:
        points += 50
    if total % 0.25 == 0:
        points += 25
    return points

def pointsFromItems(items):
    return (len(items)//2)*5

def calculatePoints(receipt):
    points = 0

    points = points + alnumPoints(receipt.validated_data["retailer"])
    points = points + pointsFromTotal(receipt.validated_data["total"])
    points = points + pointsFromItems(receipt.validated_data["items"])
    print(points)

    return points

