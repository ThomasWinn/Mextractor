import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup

class myanimelist:
    def top (self, ctx: discord.Context, type: str, url: str, num: int = 5) -> None:
        base_url = 'https://myanimelist.net/topmanga.php?type='
        search_url = base_url + type

        r = requests.get(search_url)

        soup = BeautifulSoup(r.content, 'html5lib')

        table = soup.find('table', attrs={'class':'top-ranking-table'})

        list_of_tr = table.findAll('tr', attrs={'class':'ranking-list'})

        ranking_list = []

        # TODO: Create Embeds for each msg, for last one, send a left and right arrow depending if it can go back or forwards, create a on_reaction event for when a msg is reacted to -> create a check so the bot doesn't trigger the on_reaction.
        # https://stackoverflow.com/questions/52058626/discord-py-check-if-user-reacts-with-a-specific-emoji
        # https://discordpy.readthedocs.io/en/rewrite/api.html?highlight=on%20reaction#discord.on_reaction_add
        for i in range(len(list_of_tr)):
            
            # if it's the last add the arrow emote.
            if (i == len(list_of_tr) - 1):
                rank_info = {}
            
                rank_info['rank'] = list_of_tr[i].td.span.text # tr.td.span.text
                rank_info['title'] = list_of_tr[i].td.div.h3.a.text
                rank_info['thumbnail'] = list_of_tr[i].td.a.img['data-src']
                rank_info['link'] = list_of_tr[i].td.div.h3.a['href']

                book_info = list_of_tr[i].td.div.div[1].text
                split_string = book_info.split(')')
                book_type = split_string[0] + ')'
                rank_info['type'] = book_type

                ranking_list.append(rank_info)

                # TODO: create embeds

            else:

                rank_info = {}
                
                rank_info['rank'] = list_of_tr[i].td.span.text # tr.td.span.text
                rank_info['title'] = list_of_tr[i].td.div.h3.a.text
                rank_info['thumbnail'] = list_of_tr[i].td.a.img['data-src']
                rank_info['link'] = list_of_tr[i].td.div.h3.a['href']

                book_info = list_of_tr[i].td.div.div[1].text
                split_string = book_info.split(')')
                book_type = split_string[0] + ')'
                rank_info['type'] = book_type

                ranking_list.append(rank_info)

                # TODO: create embeds

    def search(self, ctx: discord.Context, to_search: str, search_type: str) -> None:
        search = to_search.replace(' ', '%20')
        search_url = 'https://myanimelist.net/search/all?q={}&cat=all'.format(search)
        
        r = requests.get(search_url)

        soup = BeautifulSoup(r.content, 'html5lib')

        div = soup.find('table', attrs={'class':'js-scrollfix-bottom-rel'})

        if (search_type == 'anime'):
            article = div.article[0]
        elif (search_type == 'manga'):
            article = div.article[1]
        elif (search_type == 'user'):
            article = div.article[2]

        list_of_div = article.findAll('div', attrs={'class':'list di-t w100'})

        # TODO: do soemthing with all manga results



        


            

