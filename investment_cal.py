# Version 1: A basic investment calculator
initial_investment = 1000
final_value = 1200

profit = final_value - initial_investment
return_pct = (profit / initial_investment) * 100
years = 3
annualized_return = ((final_value / initial_investment) ** (1 / years) - 1) * 100
print(f"Annualized Return: {annualized_return:.2f}%")
print("Investment Calculator")
print(f"Initial Investment: ${initial_investment}")
print(f"Final Value: ${final_value}")
print(f"Profit: ${profit}")
print(f"Investment Return: {return_pct:.2f}%")





















