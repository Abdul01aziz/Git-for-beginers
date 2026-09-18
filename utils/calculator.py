'''this is a calculator module that provides basic arithmetic operations.
and it is used in the main.py file to perform calculations. and i am 
adding this just to do github fetch options'''

'add function'
def add_nmus(a,b):
    return a + b
'divide function'
def divide_nmus(a,b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
'subtract function'
def subtract_nmus(a,b):
    return a - b
'power function'
def power_nmus(a,b):
    return a ** b
'multiply function'
def multiply_nmus(a,b):
    return a * b

def abc():
    print("Delhi is capital ")