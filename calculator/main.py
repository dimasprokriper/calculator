try: 
    equation = float(input("Enter what you want to calculate: "))
    result = eval(equation)
    print(result)
except (ValueError, ZeroDivisionError, SyntaxError):
    print("Invalid input")
