from django.test import TestCase
from datetime import date, time
import numpy as np
from receipts.services.pointsCalculation import (
    alnumPoints, pointsFromTotal, pointsFromItems, pointsFromDate, pointsFromTime, calculatePoints
)


class TestPointsCalculation(TestCase):
    
    def testAlnumPoints(self):
        """Test that alphanumeric characters in retailer names are counted correctly."""
        self.assertEqual(alnumPoints("BestBuy123"), 10)  # 10 alnum chars
        self.assertEqual(alnumPoints("Shop!@#"), 4)  # Only 4 alnum chars
        self.assertEqual(alnumPoints(" "), 0)  # No alnum chars

    def testPointsFromTotal(self):
        """Test points awarded based on total amount rules."""
        self.assertEqual(pointsFromTotal(50.00), 75)  # Round + Multiple of 0.25 50+25 points
        self.assertEqual(pointsFromTotal(25.00), 75)  # Round + Multiple of 0.25 50+25 points
        self.assertEqual(pointsFromTotal(30.51), 0)  # No matching rules

    def testPointsFromItems(self):
        """Test points awarded based on item rules."""
        items = [
            {"shortDescription": "ABC", "price": "10.00"},  # Length 3 +2 points
            {"shortDescription": "XYZ", "price": "15.00"}   # Length 3 +3 points
        ]
        self.assertEqual(pointsFromItems(items), 10)  # 5 (pair) + 2 + 3 points

        items = [{"shortDescription": "Longer Item", "price": "10.00"}]
        self.assertEqual(pointsFromItems(items), 0)  # No multiple-of-3 descriptions

    def testPointsFromDate(self):
        """Test points awarded for odd purchase dates."""
        self.assertEqual(pointsFromDate("2024-03-05"), 6)  # 5th is odd +6 points
        self.assertEqual(pointsFromDate("2024-03-06"), 0)  # 6th is even +0 points

    def testPointsFromTime(self):
        """Test points awarded for purchases between 2PM and 4PM."""
        self.assertEqual(pointsFromTime(time(14, 30)), 10)  # +10 points
        self.assertEqual(pointsFromTime(time(16, 00)), 0)  # Out of range
        self.assertEqual(pointsFromTime(time(13, 59)), 0)  # Before range