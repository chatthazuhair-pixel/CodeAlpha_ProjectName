import streamlit as st
stock_prices = {
    "AAPL": 332,
    "AMZN": 256,
    "TSLA": 365,
    "NVDA": 218,
    "GOOG": 335,
    "MSFT": 495,
    "META": 648,
}

st.title("Stock Portfolio Tracker")
st.write("Calculate the total value of your stock investments.")

# Stock input
stock = st.text_input("Enter stock symbol:")

# Quantity input
quantity = st.number_input(
    "Enter quantity:",
    min_value=1,
    step=1
)

# Calculate button
if st.button("Calculate Investment"):

    stock = stock.upper()

    # Check whether the stock exists
    if stock not in stock_prices:
        st.error("Stock not available.")
        st.write("Available stocks:", ", ".join(stock_prices.keys()))

    else:
        price = stock_prices[stock]

        investment = price * quantity

        st.success("Investment calculated!")

        st.write(f"Stock: {stock}")
        st.write(f"Quantity: {quantity}")
        st.write(f"Price per share: ${price}")
        st.write(f"Investment value: ${investment}")