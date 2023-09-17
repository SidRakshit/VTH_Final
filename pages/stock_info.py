import streamlit as st
import DB_Access as dbs
import Price_Functions as pf
import json

st.title("Trade")
temp_user = "tempUser@gmail.com"

import server as sv

with open('output.txt', 'r') as file:
    # Load the contents of the file as a JSON object
    data = json.load(file)

user_id = data["userinfo"]["email"]

proper_stock_id = False

def calculate_quantity(userID, stockID):
    # Get all trades for the user and stock using the previous function
    trades_for_user_and_stock = dbs.get_user_stock_trades(userID, stockID)
    
    # Initialize a counter for the quantity
    total_quantity = 0
    
    # Loop through each trade and update the total_quantity
    for trade in trades_for_user_and_stock:
        if trade["is_buy"]:
            total_quantity += (int)(trade["qty"])
        else:
            total_quantity -= (int)(trade["qty"])
    
    return total_quantity


stock_id = st.text_input("Stock ID", placeholder="Enter Stock ID")

stock_col_1, stock_col_2, stock_col_3 = st.columns(3)

with stock_col_1:
    if stock_id:
        price = pf.get_price(stock_id, False)
        if price == "Error":
            st.write(price + ": Please Enter Correct Stock ID")
        else:
            st.write(pf.get_company_name(stock_id))
            proper_stock_id = True

with stock_col_2:
    if stock_id:
        price = pf.get_price(stock_id, False)
        if price != "Error":
            st.write('Stock price: ' + price)
            proper_stock_id = True

with stock_col_3:
    if stock_id:
        price = pf.get_price(stock_id, False)
        if price != "Error":
            st.write("Quantity in stock: " + str(calculate_quantity(user_id, stock_id)))

qty = st.text_input("Quantity", placeholder="Enter quantity")

users_db = dbs.db.Users

user_data = users_db.find_one({"email_id": user_id})

# Check if the user exists in the database
if not user_data:
    st.write(f"Error: User {user_id} not found in the database.")
else:
    user_budget = user_data["budget"]


st.write("Budget: $", str(user_budget)) 

# Check if Quantity input is a valid number
try:
    qty_as_int = int(qty)
    valid_qty = True
except ValueError:
    valid_qty = False
    if qty != "":
        st.write("Error: Please enter a valid number in the Quantity field.")

trade_col_1, trade_col_2 = st.columns(2)

if proper_stock_id and valid_qty:
    trade_value = int(qty) * float(pf.get_price(stock_id, True))

with trade_col_1:
    # BUY button
    if st.button("BUY") and valid_qty:
        if trade_value <= user_budget:
            dbs.execute_trade(user_id, stock_id, qty_as_int, float(pf.get_price(stock_id, True)), True)
            #edit budget here
            new_budget = user_budget - trade_value
            users_db.update_one({"email_id": user_id}, {"$set": {"budget": new_budget}})
            
            st.write(qty + " stocks of " + stock_id + " bought by " + user_id)
        else:
            st.write("Trade value $" + str(trade_value) + " exceeds budget")

with trade_col_2:
    # SELL button
    if st.button("SELL") and valid_qty:
        current_quantity = calculate_quantity(user_id, stock_id)
        if current_quantity >= qty_as_int:
            dbs.execute_trade(user_id, stock_id, qty_as_int, float(pf.get_price(stock_id, True)), False)
            st.write("Sold by " + user_id)
            new_budget = user_budget + trade_value
            users_db.update_one({"email_id": user_id}, {"$set": {"budget": new_budget}})
        else:
            st.write("Error: You don't have enough stock to sell.")

