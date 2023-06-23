# Stock Price API

![Logo of the Project](https://cdn.pixabay.com/photo/2015/02/20/06/19/stock-exchange-642896_1280.jpg)

This script is a simple web scraper that retrieves the stock prices for a given list of ISINs (International Securities Identification Numbers) from Tradegate. It utilizes the requests library to send HTTP requests, the BeautifulSoup library to parse HTML content, and the fake_useragent library to generate random user agents.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Installing
1. Make sure you have Python installed on your system (version 3.6 or later).

2. Clone the repository to your local machine
```
git clone https://github.com/JiGro/Stock_Price_Api.git
```

3. Install the required packages
```
pip install -r requirements.txt
```

4. Create a list of ISINs for which you want to retrieve the stock prices
```
isin_list = ["DE000A1EWWW0", "DE0008404005", "DE000BASF111", "DE000BAY0017", "DE0005200000", "DE0005190003", "DE0005439004", "DE0006062144"]
```

5. Run the code using the following command:
```
python tradegate_api.py
```

## Authors
- **Jimmy (JiGro)** - *Initial work* - [My Github Profile](https://github.com/JiGro)
