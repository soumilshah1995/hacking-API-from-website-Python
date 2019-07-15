import requests
import json
import  re


class AppleStock(object):
    def __init__(self):
        self.__headers={
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Referer': 'http://www.wikipedia.org/',
    'Connection': 'keep-alive'}

        self.__query_string = {
    'ei':'IfUsXc2oJY2J5wKngriIAQ',
    'yv':'3',
    'async': 'mids:/m/07zmbvf,currencies:,_fmt:jspb'}
        self.__url = "https://www.google.com/async/finance_wholepage_price_updates"

    @property
    def get(self):
        response = requests.get(url=self.__url, headers=self.__headers,params=self.__query_string)
        data = response.text
        pattern = re.compile(r'"AAPL","+\d{2,4}[/.]\d{1,2}"')
        matches = pattern.finditer(data)
        for match in matches:
            stock_data = match.group()

        return stock_data

obj = AppleStock()
print(obj.get)