import puzzler_functions as pf
import unittest
# Name of file containing puzzles
DATA_FILE = 'puzzles_small.txt'

# Letter values
CONSONANT_POINTS = 1
VOWEL_PRICE = 1
CONSONANT_BONUS = 2

# Players' names
PLAYER_ONE = 'Player One'
PLAYER_TWO = 'Player Two'

# Menu options - includes letter types
CONSONANT = 'C'
VOWEL = 'V'
SOLVE = 'S'
QUIT = 'Q'


class TestPuzzler(unittest.TestCase):
    def test_is_win_1(self):
        actual = pf.is_win("apple", "app^e")
        self.assertFalse(actual)
        
    def test_is_win_2(self):
        actual = pf.is_win("banana", "banana")
        self.assertTrue(actual)
        
    def test_game_over_1(self):
        actual = pf.game_over("banana", "banana", "haha")
        self.assertTrue(actual)
        
    def test_game_over_2(self):
        actual = pf.game_over("banana", "^^^^^^", QUIT)
        self.assertTrue(actual)
        
    def test_bonus_letter_1(self):
        actual = pf.bonus_letter("anti-wrinkle cream soda",
                                 "a^ti-wri^kle cream soda",
                                 "n")
        self.assertTrue(actual)
        
    def test_bonus_letter_2(self):
        actual = pf.bonus_letter("anti-wrinkle cream soda",
                                 "a^ti-wri^kle cream soda",
                                 "t")
        self.assertFalse(actual)
        
        
    def test_bonus_letter_3(self):
        actual = pf.bonus_letter("heara-smare",
                                         "h^^^^-smart",
                                         "t")
        self.assertFalse(actual)
        
        
    def test_update_letter_view_1(self):
        actual = pf.update_letter_view("where's taldo?", "where's xaldo?", 8, "a")
        self.assertEqual(actual, "x")
    
    def test_update_letter_view_2(self):
        actual = pf.update_letter_view("where's waldo?", "where's ^aldo?", 8, "w")
        self.assertEqual(actual, "w")
            
    def test_update_letter_view_3(self):
        actual = pf.update_letter_view("where's waldo?", "where's wa^do?", -4, "a")
        self.assertEqual(actual, "^")

    def test_calculate_score_1(self):
        actual = pf.calculate_score(0, 0, CONSONANT)
        self.assertEqual(actual, 0)
        
    def test_calculate_score_2(self):
        actual = pf.calculate_score(10, 3, CONSONANT)
        self.assertEqual(actual, 13)

    def test_calculate_score_3(self):
        actual = pf.calculate_score(10, 3, VOWEL)
        self.assertEqual(actual, 9)

    def test_next_player_1(self):
        actual = pf.next_player(PLAYER_ONE, 3)
        self.assertEqual(actual, PLAYER_ONE)
        
    def test_next_player_2(self):
        actual = pf.next_player(PLAYER_ONE, 0)
        self.assertEqual(actual, PLAYER_TWO)
        
    def test_next_player_3(self):
        actual = pf.next_player(PLAYER_TWO, 3)
        self.assertEqual(actual, PLAYER_TWO)
        
    def test_next_player_4(self):
            actual = pf.next_player(PLAYER_TWO, 0)
            self.assertEqual(actual, PLAYER_ONE)
        
    
if __name__ == '__main__':
    
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPuzzler)
    unittest.TextTestRunner(verbosity=2).run(suite)