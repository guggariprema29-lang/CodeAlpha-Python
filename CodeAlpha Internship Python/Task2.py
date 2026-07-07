# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 145
}

portfolio = {}
total_investment = 0

print("===== Stock Portfolio Tracker =====")
print("Available Stocks:", ", ".join(stock_prices.keys()))

# Number of different stocks
n = int(input("Enter the number of stocks you want to add: "))

for i in range(n):
    stock = input("\nEnter stock name: ").upper()

    if stock in stock_prices:
        quantity = int(input("Enter quantity: "))
        portfolio[stock] = quantity
    else:
        print("Stock not available!")

# Calculate total investment
print("\n===== Portfolio Summary =====")
for stock, quantity in portfolio.items():
    value = stock_prices[stock] * quantity
    total_investment += value
    print(f"{stock} - Quantity: {quantity}, Price: ${stock_prices[stock]}, Value: ${value}")

print("\nTotal Investment Value: $", total_investment)

# Save to a text file (Optional)
with open("portfolio.txt", "w") as file:
    file.write("Stock Portfolio Summary\n")
    file.write("------------------------\n")

    for stock, quantity in portfolio.items():
        value = stock_prices[stock] * quantity
        file.write(f"{stock} - Quantity: {quantity}, Value: ${value}\n")

    file.write(f"\nTotal Investment Value: ${total_investment}")

print("\nPortfolio details saved successfully in 'portfolio.txt'")