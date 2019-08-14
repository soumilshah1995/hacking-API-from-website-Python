
__Autho3__ ="Soumil Nitn Shah"
__Version__ = "0.0.1"


import requests
from bs4 import BeautifulSoup
import random


def random_proxy():
    url = 'https://www.sslproxies.org/'

    headers = {
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'en-US,en;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Referer': 'http://www.wikipedia.org/',
        'Connection': 'keep-alive',
    }


    r = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')

    random_ip = []
    random_port = []

    # Get the Random IP Address
    for x in soup.findAll('td')[::8]:
        random_ip.append(x.get_text())

    # Get Their Port
    for y in soup.findAll('td')[1::8]:
        random_port.append(y.get_text())

    # Zip together
    z = list(zip(random_ip,random_port))

    number = random.randint(0, len(z)-50)
    ip_random = z[number]

    ip_random_string = "{}:{}".format(ip_random[0],ip_random[1])


    proxy = {'https':ip_random_string}

    return proxy


def proxy_request(request_type, url, **kwargs):
    while True:
        try:
            proxy = random_proxy()
            print("{} using proxy".format(proxy))
            r = requests.request(request_type, url, proxies=proxy, timeout=8, **kwargs)
            return r
            break
        except:
            pass

def main():
    headers = {
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'en-US,en;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Referer': 'http://www.wikipedia.org/',
        'Connection': 'keep-alive',
    }

    params= {
        'apiKey': 'd522aa97197fd864d36b418f39ebb323',
        'format': 'json',
        'geocode': '42.361145,-71.057083',
        'language': 'en-US',
        'units':'e'
    }

    r2 = proxy_request(request_type='get', url='https://api.weather.com/v2/turbo/vt1observation',headers=headers, params=params)
    r2_data = r2.json()

    dew_point = r2_data["vt1observation"]["dewPoint"]
    feelsLike = r2_data["vt1observation"]["feelsLike"]
    humidity = r2_data["vt1observation"]["humidity"]
    observationTime = r2_data["vt1observation"]["observationTime"]
    temperature = r2_data["vt1observation"]["temperature"]
    visibility = r2_data["vt1observation"]["visibility"]
    windspeed = r2_data["vt1observation"]["windSpeed"]
    winddegree = r2_data["vt1observation"]["windDirDegrees"]
    winddirection = r2_data["vt1observation"]["windDirCompass"]

    return dew_point,feelsLike,humidity,observationTime,temperature,visibility,windspeed,winddegree,winddirection


if __name__ == "__main__":
    print(main())
