from calculator import add,subt,mul,div
import pytest
def test_addition():
    assert add(2,3)==5
    assert add(3,-7)==-4

def test_multiply():
    assert mul(4,-5)==-20
    assert mul(2,1)==2

def test_divide():
    assert div(5,1)==5

def test_subtract():
    assert subt(9,7)==2

def test_str():
    with pytest.raises(TypeError):
        add("cat")
#this means if someone enters a string in the calcultaor , then the calculator will raise TypeError and it will not be taken as input!!!!