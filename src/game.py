from bs4 import BeautifulSoup

class Game:
    def __init__(self, game_html):
        self.game_html = game_html
        self.link = game_html['href']
        self.appid = game_html['data-ds-appid']
        self.name = game_html.find('span', class_='title').text.replace('\n', '')
        self.check_discounted_price()
        
    def check_discounted_price(self):
        prices_html = self.game_html.find('div', class_='col search_price discounted responsive_secondrow')
        
        try:
            prices = prices_html.text.strip().split('zł')
            prices.pop(-1)
            self.price = prices[0]
            self.discounted_price = prices[1]
        except:
            self.discounted_price = "No discount"
            self.check_normal_price()

    def check_normal_price(self):
        price_html = self.game_html.find('div', class_='col search_price_discount_combined responsive_secondrow')

        try:
            if (price_html.text.strip() == ''):
                self.price = 'Not available yet'
                self.is_available = False
            else:
                self.is_available = True
                self.price = price_html.text.strip()
        except:
            print('error')