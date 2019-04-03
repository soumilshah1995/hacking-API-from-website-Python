
import requests

headers = {
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Referer': 'http://www.wikipedia.org/',
    'Connection': 'keep-alive',
}

url = 'https://text-to-speech-demo.ng.bluemix.net/api/v1/synthesize?t'

params= {
            'text': 'hello everyone i am going to teach you python',
            'voice': 'en-US_AllisonV2Voice',
            'download': True,
            'accept': 'audio/mp3'
}

response = requests.get(url, headers=headers,params=params)
print(response.text)


with open('hackerrr.mp3','wb') as f:
    f.write(response.content)



