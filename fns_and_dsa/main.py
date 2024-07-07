def perform_operation():
   def add(x, y):
      return x + y
   def subtraction(x, y):
      return x - y
   def divide(x, y):
         if y != 0:
             return x % y 
         else:
            return "Error: division by 0"  
   def multiplication(x, y):
      return x * y
perform_operation()