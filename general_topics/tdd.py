import unittest


class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'Hello world'

        self.assertEqual(s.split(' '), ['Hello', 'world'])

        with self.assertRaises((TypeError, ValueError)):
            s.split(2)
            s.split('')


if __name__ == '__main__':
    unittest.main()
