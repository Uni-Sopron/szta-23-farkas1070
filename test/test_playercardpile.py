import sys
import unittest

sys.path.append(
    "C://Users//SIMONMARCI//Desktop//firstangularproject//my-app//szta-23-farkas1070//LostCities"
)


from LostCities.Expeditioncard import Expeditioncard
from LostCities.Playercardpile import Playercardpile
from LostCities.Wagercard import Wagercard


class TestPlayercardpile(unittest.TestCase):
    def setUp(self):
        self.playercardpile = Playercardpile("color")

    def test_calculate_result(self):
        # Add some cards to the playercardpile
        self.playercardpile.cardarray.append(Wagercard("color"))
        self.playercardpile.cardarray.append(Wagercard("color"))
        self.playercardpile.cardarray.append(Wagercard("color"))
        self.playercardpile.cardarray.append(Wagercard("color"))
        self.playercardpile.cardarray.append(Wagercard("color"))

        self.playercardpile.cardarray.append(Expeditioncard(10, "color"))
        self.playercardpile.cardarray.append(Expeditioncard(5, "color"))
        self.playercardpile.cardarray.append(Expeditioncard(7, "color"))

        # Call the calculate_result() method
        result = self.playercardpile.calculate_result()

        # Assert that the result is calculated correctly
        expected_sum = 10 + 5 + 7
        expected_wager_multiplier = 5 + 1  # 5 wagercards
        expected_subtotal = expected_sum - self.playercardpile.EXPEDITIONCOST
        expected_result = expected_subtotal * expected_wager_multiplier

        self.assertEqual(result, expected_result)

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
