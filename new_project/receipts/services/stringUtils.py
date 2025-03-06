def alnumPoints(retailer):
    points = 0
    for char in retailer:
        if char.isalnum():
            points += 1
    return points

