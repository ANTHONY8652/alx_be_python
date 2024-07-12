def safe_divide(numerator, denominator):
    try:
        result = float("numerator") / float("denominator")
    
    except ZeroDivisionError:
        return "Error: cannot divide by zero"
    
    except ValueError:
        return "Error: Please enter numeric values only"
    
    finally:
        print(f"The result of the division is {result:.1f}")
