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


def test_calculator_subtraction():
    calculator_obj = Calculator()
    subtract_result = calculator_obj.subtract(80)
    assert  subtract_result == -80
    subtract_result = calculator_obj.subtract(-20)
    assert  subtract_result == -60
