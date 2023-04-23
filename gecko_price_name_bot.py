
"""
You need to set PRICE_BOT_TOKEN_.. variable. Example PRICE_BOT_TOKEN_BITCOIN=discord bot token
"""
from discord.ext import commands
import discord
from asyncio import sleep
import aiohttp, asyncio
import json
import sys
import traceback
import datetime, time
import os, sys
import argparse


parser = argparse.ArgumentParser()

parser.add_argument('--coin', dest='coin_name', type=str, help='Set coin name (Example: bitcoin)')
parser.add_argument('--decimal', dest='decimal', type=str, help='Set decimal place (Example: 2)')
args = parser.parse_args()

if not args.coin_name:
    print("Please set --coin! Check https://www.coingecko.com/en/api/documentation!")
    sys.exit()

if not args.decimal:
    print("Please set --decimal! Example --decimal=2")
    sys.exit()

coin_name = args.coin_name
decimal_places = args.decimal
try:
    decimal_places = int(decimal_places)
    if decimal_places < 0:
        print("Error with decimal value!")
        sys.exit()        
except ValueError:
    print("Error with decimal value!")
    sys.exit()

bot_token = os.environ.get('PRICE_BOT_TOKEN_{}'.format(coin_name.upper().replace("-", "_")))
if bot_token is None:
    print("Please set environment variable PRICE_BOT_TOKEN_{}".format(coin_name.upper()))
    sys.exit()

# API from: https://www.coingecko.com/en/api/documentation

async def gecko_coin_data(url: str, timeout: int=30):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                url,
                headers={'Content-Type': 'application/json'},
                timeout=timeout
            ) as response:
                if response.status == 200:
                    res_data = await response.read()
                    res_data = res_data.decode('utf-8-sig')
                    await session.close()
                    decoded_data = json.loads(res_data)
                    return decoded_data
    except Exception as e:
        traceback.print_exc(file=sys.stdout)
    return None

class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    async def on_ready(self):
        print("Bot is online {}.".format(self.user.name))
        print("Invite link: https://discord.com/oauth2/authorize?client_id={}&scope=bot".format(self.user.id))
    
    async def setup_hook(self) -> None:
        self.coin_name = coin_name
        self.bg_task = self.loop.create_task(self.background_task())

    async def background_task(self):
        await self.wait_until_ready()
        while not self.is_closed():
            previous_nick = {}
            previous_status = None
            try:
                url = "https://api.coingecko.com/api/v3/coins/" + self.coin_name + "?localization=false&tickers=true&market_data=true&community_data=false&developer_data=false&sparkline=false"
                get_coin_data = await gecko_coin_data(url)
                if get_coin_data is None:
                    await sleep(10.0)
                    continue
                if "error" in get_coin_data:
                    print("Can't fetched {} from coingecko!".format(self.coin_name))
                    await sleep(30.0)
                    continue
                nick_me = f"{get_coin_data['symbol'].upper()} ${get_coin_data['market_data']['current_price']['usd']:.{decimal_places}f}"
                percentage_24h = get_coin_data['market_data']['price_change_percentage_24h']
                p_place = 2
                status_me = f"24h ($): {percentage_24h:.{p_place}f}% ↘️"
                if percentage_24h > 0:
                    status_me = f"24h ($): +{percentage_24h:.{p_place}f}% ↗️"
                for guild in self.guilds:
                    me = guild.me
                    try:
                        if str(guild.id) not in previous_nick or (str(guild.id) in previous_nick and previous_nick[str(guild.id)] != nick_me):
                            await me.edit(nick=nick_me)
                            print("{} Change Bot name guild {} to {}!".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), guild.name, nick_me))
                            previous_nick[str(guild.id)] = nick_me
                        if previous_status != status_me:
                            await client.change_presence(activity=discord.Game(name=status_me))
                            previous_status = status_me
                            print("{} Set status to {}!".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), previous_status))
                        await sleep(5.0)
                    except Exception as e:
                        traceback.print_exc(file=sys.stdout)
            except Exception as e:
                traceback.print_exc(file=sys.stdout)
            await sleep(90.0)

intents = discord.Intents.default()
client = MyClient(intents=discord.Intents.default())
client.run(os.environ.get('PRICE_BOT_TOKEN_{}'.format(coin_name.upper().replace("-", "_"))))
