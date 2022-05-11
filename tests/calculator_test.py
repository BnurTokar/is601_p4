#Calculator class addition test
#Calculator class subtraction test
#Calculator class multiplication test
#Calculator class division test
#Calculator class zero_division_exception test
from calculator import Calculator

def test_calculator_addition():
    calculator_obj = Calculator()
    addition = 0
    assert addition == 0
    addition = calculator_obj.add(1)
    assert  addition == 1
    addition = calculator_obj.add(16)
    assert  addition == 17
