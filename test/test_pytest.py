import pytest

from python.calc import Cals
class TestCalc:
    def setup(self):
        self.cals=Cals()
    def test_add(self):
        result=self.cals.add(1,2)
        assert 3 == result
    def test_div(self):
        result=self.cals.div(2,2)
        assert  1 == result
    def test_div1(self):
        result=self.cals.div(2,2)
        assert  1 == result

if __name__=='__main__':
    pytest.main(['-vs','test_pytest.py::TestCalc::test_div'])