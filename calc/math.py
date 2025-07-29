import pytest

def addition(x,y):
    return x+y
print("Addition of two numbers: ",addition(2,7))
# @pytest.fixture
def substraction(x,y):
    return x-y
print("Substraction of two numbers: ",substraction(2,7))
def multiplication(x,y):
    return x*y
print("multiplication of two numbers: ",multiplication(2,7))


def add():
    return None

def subtract():
    return None

def multiply():
    return None