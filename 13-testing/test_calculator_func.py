
from calculator import add

def setup_module():
    print('module set up')

def teardown_module():
    print('module teardown')

def setup_function():
    print('function set up')

def teardown_function():
    print('function teardown')

def test_add_one_and_one():
    result = add(1, 1)
    assert result == 2