import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

def tradegate_api(stock_isin):
    agent = UserAgent()
    user_agent = agent.random
    headers = {'User-Agent': user_agent}
    print("*** Request  ISIN: " + isin + " with user agent " + user_agent + " ***")
    data = requests.get('https://www.tradegate.de/orderbuch.php?isin=' + stock_isin, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    stock_price = soup.find("td", attrs={"class": "longprice"}).get_text()
    stock_price = stock_price.replace(' ', '').replace('.', '').replace(',', '.')
    stock_price = float(stock_price.strip())
    return stock_price

isin_list = ["DE000A1EWWW0", "DE0008404005", "DE000BASF111", "DE000BAY0017", "DE0005200000", "DE0005190003", "DE0005439004", "DE0006062144"]

for isin in isin_list:
    isin_price = tradegate_api(isin)
    print("Stock price: " + str(isin_price))
