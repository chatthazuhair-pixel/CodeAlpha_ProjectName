def main():
    stock_prices = {
        "AAPL": 332,
        "TSLA": 365,
        "MSFT": 495,
        "GOOGL": 335,
        "AMZN": 256,
        "META": 650,
        "NVDA": 218,
    }

    total_investment = 0

    print("=== Stock Portfolio Tracker ===")

    while True:
        stock = input("\nEnter stock symbol (or 'done' to finish): ").upper()

        if stock == "DONE":
            break

        if stock not in stock_prices:
            print("Stock not available. Please choose a stock from the list.")
            print("Available stocks:", ", ".join(stock_prices.keys()))
            continue

        quantity = int(input("Enter quantity: "))

        price = stock_prices[stock]
        investment = price * quantity

        total_investment += investment

        print(f"{stock}: {quantity} shares × ${price} = ${investment}")

    print("\n------------------------------")
    print(f"Total Investment: ${total_investment}")
    print("------------------------------")


if __name__ == "__main__":
    main()