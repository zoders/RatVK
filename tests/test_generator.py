import unittest

from project import generator


class test_generator(unittest.TestCase):
    def test_sample_single_word(self):
        words = ('foo', 'bar', 'foobar')
        word = generator.sample(words)
        self.assertTrue(type('str') == type(word), "word is not str")

    def test_sample_multiple_words(self):
        words = ('foo', 'bar', 'foobar')
        n = 2
        words = generator.sample(words, n)
        self.assertTrue(len(words) == n, "n != " + str(n))

    def test_generate_buzz_of_at_least_five_words(self):
        phrase = generator.generate_buzz()
        self.assertTrue(len(phrase.split()) == 5, "there is more then 5 words")


if __name__ == '__main__':
    unittest.main()
