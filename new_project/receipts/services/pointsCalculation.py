import numpy as np
from datetime import time

def alnumPoints(retailer):
    points = 0
    for char in retailer:
        if char.isalnum():
            points += 1
    return points

def pointsFromTotal(total):
    points = 0
    total = float(total)
    if total % 1 == 0:
        points += 50
    if total % 0.25 == 0:
        points += 25
    return points

def pointsFromItems(items):
    points = 0

    points = points + (len(items) // 2) * 5
    for item in items:
        if len(item["shortDescription"]) % 3 == 0:
            points = points + np.ceil(float(item["price"]) * 0.2)
    return points

def pointsFromDate(date):
    day = int(str(date).split("-")[2])
    if day % 2 == 1:
        return 6
    else:
        return 0

def pointsFromTime(purchaseTime):
    if purchaseTime > time(14, 0) and purchaseTime < time(16, 0):
        return 10
    else:
        return 0

def calculatePoints(receipt):
    points = 0
    data = receipt.validated_data

    points = points + alnumPoints(data["retailer"])
    points = points + pointsFromTotal(data["total"])
    points = points + pointsFromItems(data["items"])
    points = points + pointsFromDate(data["purchaseDate"])
    points = points + pointsFromTime(data["purchaseTime"])

    return points

