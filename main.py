from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import discord
from discord.ext import commands
from textwrap3 import wrap
import feedparser
from datetime import timedelta, datetime

bot = commands.Bot(command_prefix='?', description="This is a Discord Parser RSS Bot", help_command=None)
token = "Secret Token"

"""
Parser function
"""

@bot.command()
async def parse(ctx, link):
    page = requests.get(link)
    soup = BeautifulSoup(page.text, "html.parser")
    soup_text = soup.get_text()
    if len(soup_text) > 2000:
        longMsg = wrap(soup_text, 2000)
        for i in longMsg: 
            await ctx.send(i)
    await ctx.send(soup_text)

"""
RSS function
"""

FEED_URL = ['https://something.com/feeds/rss.xml']

@bot.command()
async def rss_daily(ctx):
    day_ago = datetime.now() - timedelta(days=1)
    for feed in FEED_URL:
        rss_feed = feedparser.parse(feed)
        for entry in rss_feed.entries:
                published_date = entry.published
                published_date = published_date[5:-6]
                published_date_obj = datetime.strptime(published_date, '%d %b %Y %H:%M:%S')
                if published_date_obj > day_ago:
                    await ctx.send(entry.links[0].href)

"""
Other functions
"""
@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def help(ctx):
    await ctx.send("""
    Discord Parser RSS bot: Designed to bring your daily rss feed and parse links, printing content directly to chat
    -Prefix is '?'
    -help -- this command, describes bot and its commands
    -ping -- answers with 'pong', tests bot responsing
    -parse [link] -- prints web-site text into chat (prints everything, not only main text)
    -rss_daily -- prints to chat links of rss feeds included into bot code
    """)

bot.run(token)