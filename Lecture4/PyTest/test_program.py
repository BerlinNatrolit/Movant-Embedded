# A Very short PyTest-example.
import pytest           # needed for approx-function below.
from program import *   # file with functions we want to test.

def test_area_of_square():
    assert area_of_square(2) == 3

def test_area_of_rectangle():
    assert area_of_rectangle(2,3) == 6

def test_area_of_cirlce():
    assert area_of_circle(1) == pytest.approx(3.14159)

# you can have several asserts in one test, but might not be best practice.
def test_add():
    assert add(1,2) == 3
    assert add(5.5,6.5) == 12
    assert add(0.1, 0.2) == pytest.approx(0.3)