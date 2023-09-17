import streamlit as st
import pymongo
import sys
# sys.path.append("../")


@st.cache_resource
def init_connection():
    return pymongo.MongoClient(st.secrets["mongo"]["uri"])

client = init_connection()
db = client.stockSim
# st.write(client)

current_session_user = None

def execute_trade(userID, stockID, qty, price, is_buy):
    trades = db.Trades
    trade_info = {
        "user_id": userID,
        "stock_id": stockID,
        "qty": qty,
        "is_buy": is_buy,
        "price": price
    }
    trades.insert_one(trade_info)


def get_user_stock_trades(userID, stockID):
    # Get the Trades collection
    trades = db.Trades
    
    # Create a filter for the desired userID and stockID
    trade_filter = {
        "user_id": userID,
        "stock_id": stockID
    }
    
    # Query the database using the filter
    results = trades.find(trade_filter)
    
    # Convert the results into a list and return
    return list(results)

