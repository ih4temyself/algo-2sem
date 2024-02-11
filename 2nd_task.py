
def counter_dx(string):
    digits = []
    operators = []
    
    for char in string: 
        if char.isdigit(): 
            digits.append(int(char))
        elif char == "(":
            pass
        elif char == ")":
            digit1 = digits.pop()
            digit2 = digits.pop()
            operator = operators.pop()

            digits.append(eval(f"{digit1} {operator} {digit2}"))

        else:
            operators.append(char)
            
    return digits[0]
          


string = "(1+((2+3)*(4*5)))"
print(counter_dx(string)) 