import sys

sys.path.append(
    "C://Users//SIMONMARCI//Desktop//firstangularproject//my-app//szta-23-farkas1070//LostCities"
)
import unittest

from Expeditioncard import Expeditioncard
from Playercardpile import Playercardpile
from Wagercard import Wagercard


# test ok
class TestPlayercardpile(unittest.TestCase): 
    def setUp(self):
        self.playercardpile = Playercardpile("color")

    def test_calculate_sum(self):
        # Add some cards to the playercardpile
        self.playercardpile.cardarray.append(Wagercard("color"))
        self.playercardpile.cardarray.append(Wagercard("color"))
        self.playercardpile.cardarray.append(Wagercard("color"))
        self.playercardpile.cardarray.append(Wagercard("color"))
        self.playercardpile.cardarray.append(Wagercard("color"))

        self.playercardpile.cardarray.append(Expeditioncard(10, "color"))
        self.playercardpile.cardarray.append(Expeditioncard(5, "color"))
        self.playercardpile.cardarray.append(Expeditioncard(7, "color"))

        # Call the calculate_sum() method
        self.playercardpile.calculate_sum()

        # Assert that the sum is calculated correctly
        expected_sum = 10 + 5 + 7
        self.assertEqual(self.playercardpile.sum, expected_sum)


if __name__ == "__main__":
    unittest.main()
