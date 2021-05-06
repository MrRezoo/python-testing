import unittest

from models.person import Person


class TestPerson(unittest.TestCase):

    def setUp(self):
        self.p1 = Person('rezoo', 'mob')
        self.p2 = Person('mik', 'raz')

    def tearDown(self) -> None:
        print('Done. . .')

    def test_fullname(self):
        self.assertEqual(self.p1.fullname(), 'rezoo mob')
        self.assertEqual(self.p2.fullname(), 'mik raz')

    def test_email(self):
        self.assertEqual(self.p1.email(), 'rezoomob@email.com')
        self.assertEqual(self.p2.email(), 'mikraz@email.com')


if __name__ == '__main__':
    unittest.main()
