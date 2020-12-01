import requests
from bs4 import BeautifulSoup
from game import Game

url = 'https://store.steampowered.com/search/?tags=3859%2C1685'

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

games = soup.find(id='search_resultsRows')

games_iterator = games.find_all('a', href=True)

for game_html in games_iterator:
    game = Game(game_html)
    print(game.name)
    print(game.link)
    print(game.price[0])
    print(game.price[1])
    print('\n')

