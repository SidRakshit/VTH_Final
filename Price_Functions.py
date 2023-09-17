import requests
from bs4 import BeautifulSoup

def get_price(stock, is_int):
    url = "https://www.google.com/finance/quote/"+stock+":NASDAQ"
    result = requests.get(url)
    if requests: 
        src = result.content
        soup = BeautifulSoup(src, 'lxml')
        price = soup.find('div', {'class': 'YMlKec fxKbKc'})
        if price:
            if is_int:
                price = price.text.replace('$', '').replace(',', '')
            else:
                price = price.text
            return price
        else:
            result = requests.get(url = "https://www.google.com/finance/quote/"+stock+":NYSE")
            soup = BeautifulSoup(result.content, 'lxml')
            price = soup.find('div', {'class': 'YMlKec fxKbKc'})
            if price:
                if is_int:
                    price = price.text.replace('$', '').replace(',', '')
                else:
                    price = price.text
            else:
                price = "Error"
        return price
    else:
        price = "Page not found"
        return price

def get_company_name(stock):
    # Check for the stock on NASDAQ first
    url = "https://www.google.com/finance/quote/"+stock+":NASDAQ"
    result = requests.get(url)
    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    
    # Attempt to find the company name using the potential HTML structure of Google Finance
    name = soup.find('div', {'class': 'zzDege'})

    # If the company name wasn't found on NASDAQ, check NYSE
    if not name:
        url = "https://www.google.com/finance/quote/"+stock+":NYSE"
        result = requests.get(url)
        soup = BeautifulSoup(result.content, 'lxml')
        name = soup.find('div', {'class': 'zzDege'})

    if name:
        return name.text.split("\n")[0].strip()  # Using split and strip to ensure we only get the company name
    else:
        return "Error"