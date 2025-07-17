# tests/test_grammar_corrector.py

import unittest
from app.grammar_corrector import GrammarCorrector

class TestGrammarCorrector(unittest.TestCase):
    def setUp(self):
        self.gc = GrammarCorrector()

    def test_she_go_to_park(self):
        result = self.gc.correct_text("She go to the park every day")
        self.assertEqual(result["corrected"], "She goes to the park every day.")
        self.assertIn("error", result["feedback"].lower())

    def test_he_have_two_dog(self):
        result = self.gc.correct_text("He have two dog")
        self.assertEqual(result["corrected"], "He has two dogs.")
        self.assertIn("error", result["feedback"].lower())

    def test_i_am_student(self):
        result = self.gc.correct_text("I am student")
        self.assertEqual(result["corrected"], "I am a student.")
        self.assertIn("error", result["feedback"].lower())

    def test_they_is_coming(self):
        result = self.gc.correct_text("They is coming to school now")
        self.assertEqual(result["corrected"], "They are coming to school now.")
        self.assertIn("error", result["feedback"].lower())

    def test_she_cans_play(self):
        result = self.gc.correct_text("She cans play piano very good")
        self.assertEqual(result["corrected"], "She can play the piano very well.")
        self.assertIn("error", result["feedback"].lower())

    def test_boy_eat_apple(self):
        result = self.gc.correct_text("The boy eat apple in the morning")
        self.assertEqual(result["corrected"], "The boy eats an apple in the morning.")
        self.assertIn("error", result["feedback"].lower())

    def test_friend_no_speak(self):
        result = self.gc.correct_text("My friend no speak english good")
        self.assertEqual(result["corrected"], "My friend does not speak English well.")
        self.assertIn("error", result["feedback"].lower())

    def test_we_was_go(self):
        result = self.gc.correct_text("We was go to the cinema yesterday")
        self.assertEqual(result["corrected"], "We went to the cinema yesterday.")
        self.assertIn("error", result["feedback"].lower())

    def test_she_have_big_house(self):
        result = self.gc.correct_text("She have a big house and two cat")
        self.assertEqual(result["corrected"], "She has a big house and two cats.")
        self.assertIn("error", result["feedback"].lower())

    def test_book_are_interesting(self):
        result = self.gc.correct_text("This book are very interesting and help me to learn")
        self.assertEqual(result["corrected"], "This book is very interesting and helps me to learn.")
        self.assertIn("error", result["feedback"].lower())

if __name__ == '__main__':
    unittest.main()
