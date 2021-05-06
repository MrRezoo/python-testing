import time

import pytest

from src.person import Person


class TestPerson:

    @pytest.fixture
    def setup(self):
        self.p1 = Person('rezoo', 'mob')
        self.p2 = Person('mik', 'raz')
        yield 'setup'
        time.sleep(2)

    def test_fullname(self, setup):
        assert self.p1.fullname() == 'rezoo mob'
        assert self.p2.fullname() == 'mik raz'

    def test_email(self, setup):
        assert self.p1.email() == 'rezoomob@email.com'
        assert self.p2.email() == 'mikraz@email.com'
