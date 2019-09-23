try:
    import  requests
    from bs4 import  BeautifulSoup
except Exception as e:
    print('Some Modules are Missing {}'.formate(e))


class Goldrate(object):

    def __init__(self):

        self.__headers = {
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'en-US,en;q=0.8',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Referer': 'http://www.wikipedia.org/',
            'Connection': 'keep-alive',
        }
        self.url = " https://www.paisabazaar.com/gold-rate/"

    @property
    def get(self):
        """

        :return: String value for Gold Rates
        """

        r = requests.get(url=self.url, headers=self.__headers)
        soup = BeautifulSoup(r.text, 'html.parser')

        data = soup.findAll(class_='g-6-s goldRate__price goldRatePriceHighLite')
        tem = []
        for x in data:
            val = x.text[3:]
            tem.append(val)

            break
        return tem[0]


if __name__ == "__main__":
    obj = Goldrate()
    data = obj.get
    print("Soumil Gold Rates in India :\t{}".format(data))

