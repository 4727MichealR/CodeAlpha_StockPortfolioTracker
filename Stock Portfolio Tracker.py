stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 300
}

total_value = 0

print("Stock Portfolio Tracker")

while True:
    stock = input("Enter stock name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not found!")
        continue

    quantity = int(input("Enter quantity: "))

    investment = stock_prices[stock] * quantity
    total_value += investment

    print(f"{stock}: ₹{investment}")

print("\nTotal Investment Value: ₹", total_value)

with open("portfolio.txt", "w") as file:
    file.write(f"Total Investment Value: ₹{total_value}")

print("Result saved in portfolio.txt")