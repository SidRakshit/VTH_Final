import streamlit as st
import random
import pandas as pd
import json

# Assuming you have the Price_Functions as pf imported
import Price_Functions as pf
import DB_Access as dbs

with open('output.txt', 'r') as file:
    # Load the contents of the file as a JSON object
    data = json.load(file)

user_id = data["userinfo"]["email"]

def generate_portfolio_data(user_id):
    portfolio_data = []
    trades = dbs.db.Trades
    user_trades = trades.find({"user_id": user_id})
    unique_stock_ids = {trade["stock_id"] for trade in user_trades}
    
    for stock_id in unique_stock_ids:
        stock_name = pf.get_company_name(stock_id)  # Fetch the stock name
        
        trades_for_stock = dbs.get_user_stock_trades(user_id, stock_id)
        quantity_at_hand = 0
        for trade in trades_for_stock:
            if trade["is_buy"]:
                quantity_at_hand += int(trade["qty"])
            else:
                quantity_at_hand -= int(trade["qty"])
        
        if quantity_at_hand == 0:
            continue

        total_spent = sum(float(trade["price"]) * int(trade["qty"]) for trade in trades_for_stock if trade["is_buy"])
        total_received = sum(float(trade["price"]) * int(trade["qty"]) for trade in trades_for_stock if not trade["is_buy"])
        
        investment = float(format(total_spent - total_received, '.2f'))
        avg_price_on_buy = float(format(investment / quantity_at_hand, '.2f')) if quantity_at_hand != 0 else 0.00
        
        price_response = pf.get_price(stock_id, True)
        if price_response == 'Error':
            continue
        current_price = float(format(float(price_response), '.2f'))
        current_value = float(format(quantity_at_hand * current_price, '.2f'))
        unrealised_profit_loss = float(format(current_value - investment, '.2f'))
        profit_loss_percent = float(format((unrealised_profit_loss / investment) * 100, '.2f')) if investment != 0 else 0.00

        portfolio_data.append([
            stock_id, 
            stock_name,  # Include the stock name here
            quantity_at_hand, 
            investment, 
            current_value, 
            unrealised_profit_loss, 
            profit_loss_percent
        ])
    
    return portfolio_data

def format_to_two_decimal(num):
    """Convert a number to string with 2 decimal places."""
    return "{:.2f}".format(num)

def highlight_profit_color(val):
    try:
        val = float(val)
    except:
        pass

    color = 'green' if val > 0 else 'red' if val < 0 else 'blue'
    return f'color: {color}'

def main():
    st.set_page_config(page_title="Portfolio", page_icon="📊")
    st.title("Portfolio")
    portfolio_data = generate_portfolio_data(user_id)
    df = pd.DataFrame(portfolio_data, columns=["Stock ID", "Stock Name", "Quantity", "Total Investment", "Current Cost", "Unrealised Profit/Loss", "Profit/Loss (%)"])

    df.index = range(1, len(df) + 1)
    # First, apply the highlight color
    df_styled = df.style.applymap(highlight_profit_color, subset=['Unrealised Profit/Loss'])

    # Then, format the dataframe values
    float_columns = ["Total Investment", "Current Cost", "Unrealised Profit/Loss", "Profit/Loss (%)"]
    for col in float_columns:
        df[col] = df[col].apply(format_to_two_decimal)
    
    st.dataframe(df_styled)

if __name__ == '__main__':
    main()
