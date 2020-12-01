from bs4 import BeautifulSoup

class Game:
    def __init__(self, game):
        self.link = game['href']
        prices = game.find('div', class_='col search_price discounted responsive_secondrow')
        
        try:
            self.price = price.text.replace('\n', '')
            self.price = [price.split('zł')[0], price.split('zł')[1]]
        except:
            self.price = ['Free to play', '']
        
        self.name = game.find('span', class_='title').text
