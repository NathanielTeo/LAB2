import LAB2
import mock

print("Testing Lab 2")

def test_get_user_input():
    result = []
    test_arr = [5,3,65,9]

    with mock.patch('builtins.input', return_value="5,3,65,9"):
        assert LAB2.get_user_input() == test_arr

def test_calc_average():
    result = []
    input_arr = [25,27,26]
    test = 26

    result = LAB2.calc_average(input_arr)

    assert result==test


