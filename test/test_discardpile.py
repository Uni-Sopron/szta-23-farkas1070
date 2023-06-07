import sys

sys.path.append(
    "C://Users//SIMONMARCI//Desktop//firstangularproject//my-app//szta-23-farkas1070//LostCities"
)
import unittest

from Discardpile import Discardpile
from Expeditioncard import Expeditioncard


# test ok
class TestCardPile(unittest.TestCase):
    def test_is_cardpile_empty(self):
        # Create a sample cardpile
        cardpile = Discardpile("green")

        # Assert that the cardpile is initially empty
        self.assertTrue(cardpile.is_cardpile_empty())

        # Add a card to the cardpile
        card = Expeditioncard(5, "red")
        cardpile.cardarray.append(card)

        # Assert that the cardpile is not empty after adding a card
        self.assertFalse(cardpile.is_cardpile_empty())


if __name__ == "__main__":
    unittest.main()
