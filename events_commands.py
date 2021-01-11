import discord
from discord.ext import commands
import asyncio
import os
from dotenv import load_dotenv # pip install python-dotenv
# import manga_extract as me

load_dotenv()
bot = commands.Bot(command_prefix='$')

good_emojis = [
  '<:man_gesturing_no:796524988827959346>',

]

@bot.event
async def on_ready():
  print('Logged in as {}'.format(bot.user))

# @bot.event
# async def on_message(message):
#   if (message.author == bot.user):
#     return
  
#   if (message.content.startswith('%hi')):
#     await message.channel.send('Bish Wassup!')

'''---------------------------- BOT COMMANDS ---------------------------------------------------''' 

@bot.command()
async def mal_search(ctx, *args):
    if (args[0] == 'user'):
        pass
    if (args[0] == 'manga'):
        pass

@bot.command()
async def mal_top(ctx, *args):
    if (args[0] == 'manga'):
        pass
    if (args[0] == 'doujinshi'):
        pass
    if (args[0] == 'lightnovels'):
        pass
    if (args[0] == 'manhwa'):
        pass
    if (args[0] == 'manhua'):
        pass
    if (args[0] == 'popular'):
        pass
    else:
        await ctx.send(
            """
            ``` Please use $help to see available commands and options! ( ^..^)ﾉ ```
            """
        )
        #   msg = await ctx.send("""
#     ```{} \n\n Please choose one result!```
#   """.format(manga_titles))

# # TODO: TEST os.getcwd()
# @bot.command(
#   help='Main function for extracting manga chapters into a pdf for user to download',
#   brief='Uses MangaFast.net under the hood to extract manga chapters'
# )
# async def extract(ctx, *args):

#   '''----------------SEARCH-----------'''
#   title = ""
  
#   for i in range(len(args)):
#     if (i == len(args) - 1):
#       title += args[i]
#     else:
#       title += args[i] + ' '
  
#   await ctx.send('Searching {}'.format(title))

#   title_array = me.manga_extract.search(title)

#   manga_titles = 'There are {} results when searching {}\n'.format(len(title_array), title)

#   for i in range(len(title_array)):
#     manga_titles += '[{}]  {}\n'.format(i, title_array[i]['title'])

#   # TODO: ThomasWinn, there are 2 results when searching _________
#   msg = await ctx.send("""
#     ```{} \n\n Please choose one result!```
#   """.format(manga_titles))

  
#   def check(message: discord.Message):
#     return message.author != ctx.me and message.channel == ctx.channel and message.content.isnumeric() and int(message.content) % 1 == 0 and int(message.content) >= 0 and int(message.content) <= len(title_array) - 1

#   try:
#     choice = await bot.wait_for('message', timeout=30.0, check=check) # returns back a discord.Message

#   # TODO: FIGURE OUT HOW TO ADD EMOJI ONTO PREVIOUS MESSAGES
#   except asyncio.TimeoutError:
#     await msg.add_reaction('man_gesturing_no')

#   print(choice)
#   # use choice.content

#   title_info = title_array[int(choice.content)]


#   '''----------------FIND CHAPTER-----------'''

#   # TODO : START FIGURING THIS OUT
#   chapter = me.manga_extract.find_chapter(bot, title_info['link'])
  
  




# @bot.command(
#   help='Checks if input is searchable.',
#   brief='Uses MangaFast.net to extract titles from specified input.'
# )
# async def check(ctx, *args):
#   title = ""
  
#   for i in range(len(args)):
#     if (i == len(args) - 1):
#       title += args[i]
#     else:
#       title += args[i] + ' '

#   await ctx.send('Searching {}'.format(title))

#   title_array = me.manga_extract.search(title)

#   manga_titles = 'There are {} results when searching {}\n'.format(len(title_array), title)

#   for i in range(len(title_array)):
#     manga_titles += '[{}]  {}\n'.format(i, title_array[i]['title'])

#   await ctx.send("""
#     ```{}```
#   """.format(manga_titles))

bot.run(os.getenv('TOKEN'))