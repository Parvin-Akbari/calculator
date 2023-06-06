# test file for app.py
# test craetor : parvin akbari

# import functions from app.py
from app import strCheck
from app import calculator

# test strCheck function
def test_syntax_error_start_with_mark():
    str_check = strCheck("+1")
    assert str_check == True

def test_syntax_error_end_with_mark():
    str_check = strCheck("33*")
    assert str_check == True

def test_syntax_error_one_mark():
    str_check = strCheck("1*2+3")
    assert str_check == True

def test_syntax_error_from_marks():
    str_check = strCheck("1#3")
    assert str_check == True

# test calculator function
def test_calculator_sum():
    str_calculate = calculator("2+3")
    assert str_calculate == 5

def test_calculator_minus():
    str_calculate = calculator("45-35")
    assert str_calculate == 10

def test_calculator_multiplication():
    str_calculate = calculator("2*25")
    assert str_calculate == 50

def test_calculator_Division():
    str_calculate = calculator("200/2")
    assert str_calculate == 100