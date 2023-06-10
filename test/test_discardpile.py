import unittest
from unittest.mock import patch

from LostCities.Discardpile import Discardpile


class TestCardPile(unittest.TestCase):
    def test_is_cardpile_empty(self):
        # Create a sample cardpile
        cardpile = Discardpile("green")

        with patch.object(cardpile, "cardarray", new=[]):
            # Assert that the cardpile is initially empty
            self.assertTrue(cardpile.is_cardpile_empty())

            # Add a card to the cardpile
            cardpile.cardarray.append("card")

            # Assert that the cardpile is not empty after adding a card
            self.assertFalse(cardpile.is_cardpile_empty())


if __name__ == "__main__":
    unittest.main()
