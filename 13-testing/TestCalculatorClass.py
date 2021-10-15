import pytest
from calculator import Calculator

@pytest.fixture
def calculator():
    """ Returns a Calculator instance """
    print('calculator fixture')
    return Calculator()


class TestCalculatorClass:

    def setup_class(cls):
        print('\nstartup once per class')

    def teardown_class(cls):
        print('\nteardown once per class')

    def setup_method(self):
        print('\nstartup per test')

    def teardown_method(self):
        print('\nteardown per test')

    # Tests follow from here

    def test_initial_value(self, calculator):
        assert calculator.total == 0, "initial value not set"

    def test_add_one(self, calculator):
        calculator.set(1)
        calculator.add()
        assert calculator.total == 1

    def test_add_2_and_3(self, calculator):
        calculator.set(3)
        calculator.add()
        calculator.set(2)
        calculator.add()
        assert calculator.total == 5, "add 2+3 does not equal 5"