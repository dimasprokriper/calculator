n = input("Enter 'C' to convert Celsius to Fahrenheit or 'F' to convert Fahrenheit to Celsius: ").strip().upper()
if n == 'C':
    try:
        c = input("Enter temperature in Celsius: ")
        fahrenheit = (float(c) * 9/5) + 32
        print(f"Temperature in Fahrenheit: {fahrenheit:.2f}")
    except ValueError:
        print("Please enter a valid number.")
elif n == 'F':
        try:
            f = input("Enter temperature in Fahrenheit: ")
            celsius = (float(f) - 32) * 5/9
            print(f"Temperature in Celsius: {celsius:.2f}")
        except ValueError:                 
            print("Please enter a valid number.")
else:
    print("Invalid input. Please enter 'C' or 'F'.")