from lecture3.custom_stack import Stack

def counter_dx(string):
    digits = Stack()
    operators = Stack()
    
    for char in string: 
        if char.isdigit(): 
            digits.push(int(char))
        elif char == "(":
            pass
        elif char == ")":
            digit1 = digits.pop()
            digit2 = digits.pop()
            operator = operators.pop()

            digits.push(eval(f"{digit1} {operator} {digit2}"))

        else:
            operators.push(char)
            
    return digits.pop()
          


string = "(1+((2+3)*(4*5)))"
print(counter_dx(string)) 