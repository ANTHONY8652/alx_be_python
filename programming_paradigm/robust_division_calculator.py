def safe_divide(numerator, denominator):
    try:
        result = float(numerator) / float(denominator)
    
    except ZeroDivisionError:
        print("Error: cannot divide by zero")
    
    except ValueError:
        print("Error: Please enter numeric values only")
    
    else:
        return f"The result of the division is {result}"