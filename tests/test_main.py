from src.my_app.main import say_hello, new_test

def test_say_hello():
    assert say_hello() == "Hello, World!"

def test_new_test():
    assert new_test() == "New, Test!"