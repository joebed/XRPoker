import unittest
from models.card import Card, Suit, Rank

class TestCard(unittest.TestCase):

    def test_lt_two_and_ace(self):
        two_of_hearts = Card(Rank.TWO, Suit.HEARTS)
        ace_of_spades = Card(Rank.ACE, Suit.SPADES)
        self.assertTrue(two_of_hearts < ace_of_spades)

    def test_le_two_and_ace(self):
        two_of_hearts = Card(Rank.TWO, Suit.HEARTS)
        ace_of_spades = Card(Rank.ACE, Suit.SPADES)
        self.assertTrue(two_of_hearts <= ace_of_spades)

    def test_gt_ace_and_two(self):
        two_of_hearts = Card(Rank.TWO, Suit.HEARTS)
        ace_of_spades = Card(Rank.ACE, Suit.SPADES)
        self.assertTrue(ace_of_spades > two_of_hearts)

    def test_ge_ace_and_two(self):
        two_of_hearts = Card(Rank.TWO, Suit.HEARTS)
        ace_of_spades = Card(Rank.ACE, Suit.SPADES)
        self.assertTrue(ace_of_spades >= two_of_hearts)

    def test_ge_ace_and_ace(self):
        ace_of_hearts = Card(Rank.ACE, Suit.HEARTS)
        ace_of_spades = Card(Rank.ACE, Suit.SPADES)
        self.assertTrue(ace_of_spades >= ace_of_hearts)

    def test_le_ace_and_ace(self):
        ace_of_hearts = Card(Rank.ACE, Suit.HEARTS)
        ace_of_spades = Card(Rank.ACE, Suit.SPADES)
        self.assertTrue(ace_of_spades <= ace_of_hearts)

    def test_et_king_and_king(self):
        king_of_spades = Card(Rank.KING, Suit.SPADES)
        king_of_hearts = Card(Rank.KING, Suit.HEARTS)
        self.assertTrue(king_of_spades == king_of_hearts)

    def test_et_king_and_three(self):
        king_of_spades = Card(Rank.KING, Suit.SPADES)
        three_of_hearts = Card(Rank.THREE, Suit.HEARTS)
        self.assertFalse(king_of_spades == three_of_hearts)

if __name__ == '__main__':
    unittest.main()