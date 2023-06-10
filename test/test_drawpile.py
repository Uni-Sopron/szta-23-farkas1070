import unittest

from LostCities.Drawpile import Drawpile


class TestDrawpile(unittest.TestCase):
    def test_shuffle(self):
        # Create a sample drawpile with known cards
        colors = ["red", "blue", "green"]
        numbers = [1, 2, 3]
        drawpile = Drawpile(colors, numbers)

        # Copy the original cardarray before shuffling
        original_cardarray = drawpile.cardarray[:]

        # Shuffle the drawpile
        drawpile.shuffle()

        # Assert that the cardarray has been modified after the shuffle
        self.assertNotEqual(original_cardarray, drawpile.cardarray)


if __name__ == "__main__":
    unittest.main()
