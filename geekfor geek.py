
import requests

headers = {
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Referer': 'http://www.wikipedia.org/',
    'Connection': 'keep-alive',
}

url = 'https://ide.geeksforgeeks.org/main.php'


code='''
a=input()
print(a)
'''

params= {
    'lang': 'Python3',
    'code': code,
    'input':'soumil shah',
    'save': True
}

response = requests.post(url,data=params)
print(response.json())
data = response.json()

print(data['output'])
print(data['memory'])


