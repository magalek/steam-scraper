import requests
from bs4 import BeautifulSoup
from game import Game

url = 'https://store.steampowered.com/search/?sort_by=Released_DESC&category3=1'

second_url = 'https://store.steampowered.com/search/?category3=1'

discord_url = '' 


page = requests.get(second_url)
soup = BeautifulSoup(page.content, 'html.parser')

games = soup.find(id='search_resultsRows')

games_iterator = games.find_all('a', href=True)

for game_html in games_iterator:
    game = Game(game_html)
    if (game.discounted_price == 'No discount'):
        if (game.is_available):
            game_info = f'[{game.name}](<{game.link}\>)\nPrice: {game.price}\n'
        else:
            game_info = f'[{game.name}](<{game.link}\>)\nNot available\n'
    else:
        game_info = f'###[{game.name}](<{game.link}\>)\n~~Normal price: {game.price}zł~~\n**Price on discount: {game.discounted_price}zł**\n'

    # UNCOMMENT IF DISCORD HOOK ADDED
    # data = {'content' : game_info}
    # requests.post(discord_url, data=data)
