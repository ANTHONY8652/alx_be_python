#Ask the user input for financial details 
monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))
#calculate monthly savings
monthly_savings = monthly_income - monthly_expenses
#project annual savings
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
#print projected savings
print(f"Projected savings after one year, with interest, is: {projected_savings}")