<p align="center">
  <img width="180" src="./BTIPZ.png" alt="Simple Price Tracking Bot">
  <h1 align="center">Gecko Price Tracking Bot</h1>
</p>

<!-- Table of Contents -->

<summary><h2 style="display: inline-block">Table of Contents</h2></summary>
<ul>
    <li><a href="#intro">Intro</a></li>
    <li><a href="#our-discord">Our Discord</a></li>
    <li><a href="#bot-invitation">Bot Invitation</a></li>
    <li><a href="#setup">Setup</a></li>
    <li><a href="#donation">Donation</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#credit-and-thanks-to">Credit and thanks to</a></li>
</ul>

### Intro

Easy-to-run price name Bots using CoinGecko API.

![Screenshot](https://github.com/0xBTIPZ/Gecko-Price-Bot-Names/blob/main/screenshot.jpg?raw=true)


### Our Discord

* BTIPZ: <http://join.btipz.com>

### Bot Invitation

If you don't want to run you own, the bots are public. They need only permission to change their nicknames.

* ADA: [Invite Cardano Price Bot](https://discord.com/oauth2/authorize?client_id=1099476022568681513&scope=bot&permissions=67108864)
* BNB: [Invite BinanceCoin Price Bot](https://discord.com/oauth2/authorize?client_id=1099274947668496416&scope=bot&permissions=67108864)
* BTC: [Invite Bitcoin Price Bot](https://discord.com/oauth2/authorize?client_id=1099270461914890302&scope=bot&permissions=67108864)
* DOGE: [Invite Dogecoin Price Bot](https://discord.com/oauth2/authorize?client_id=1099300147021754478&scope=bot&permissions=67108864)
* ETH: [Invite Ethereum Price Bot](https://discord.com/oauth2/authorize?client_id=1099272885782192128&scope=bot&permissions=67108864)
* FTM: [Invite Fantom Price Bot](https://discord.com/oauth2/authorize?client_id=1099298264123187240&scope=bot&permissions=67108864)
* LTC: [Invite Litecoin Price Bot](https://discord.com/oauth2/authorize?client_id=1099294186550874213&scope=bot&permissions=67108864)
* MATIC: [Invite Matic Price Bot](https://discord.com/oauth2/authorize?client_id=1099296389151858780&scope=bot&permissions=67108864)
* SOL: [Invite Solana Price Bot](https://discord.com/oauth2/authorize?client_id=1099478572487417918&scope=bot&permissions=67108864)
* XLM: [Invite Stellar Price Bot](https://discord.com/oauth2/authorize?client_id=1099303159760953435&scope=bot&permissions=67108864)
* XMR: [Invite Monero Price Bot](https://discord.com/oauth2/authorize?client_id=1099301705071480932&scope=bot&permissions=67108864)
* XTZ: [Invite Tezos Price Bot](https://discord.com/oauth2/authorize?client_id=1099304345402605649&scope=bot&permissions=67108864)

If there is any other coin/token you would like us to run, just drop by in our Discord and ask.

## Setup

You need to create a Bot through [Discord Application](https://discord.com/developers/applications). You need to run with either python3.8 or python3.10 with virtualenv. And you can run as many bots as you want with the same script. Below is an example for Bitcoin.

```
# If other coin besides Bitcoin, you need to replace PRICE_BOT_TOKEN_BITCOIN with PRICE_BOT_TOKEN_COIN_ID (All capital letter and they're from CoinGecko. If the coin id has -, replace it with _)
export PRICE_BOT_TOKEN_BITCOIN="Your Discord bot token here"
virtualenv -p /usr/bin/python3.10 ./
source bin/activate
pip3 install discord aiohttp argparse
# Example of Bitcoin
python3 --coin=bitcoin --decimal=2
```

If you run with pm2 (process monitor):

```
pm2 start `pwd`/gecko_price_name_bot.py --name "TICKERBOT-BTC" --interpreter=python3.10 -- --coin=bitcoin --decimal=2
```

The parameter `--coin`, you need to get it from CoinGecko via "API id". You need to set `--decimal` for number of decimal places of price. It should be 2 or 3.

## Donation

* ETH: 0xa497c1f93467f64b6ec93fdfcdb24de52df9779c
* TOKEN (ERC-20, BEP20, BTIPZ, etc): 0xfdaba0f1183ee4c65754f83f5ad4c4e0bd164974
* BTC: bc1qjmutqpzm7e8n9t6rzefcu64mz4fnx3tq5dk2lq
* DOGE: DCShomKiq1coV9yaGFT5vy1BzK1yp3EnrH
* LTC: MXBdw2gbDyPAUKqXTp7imzr36SjRVn2e6w
* XMR: 4Hh8CAoojaYFZPjA9R7ndGMV6kjLMg1dqKAceg6eJxSp9QUtUpY4Do6QF3931WYSSMVVCY6u6BtCjKMEAzbnZgsmJEy78v9mq2CJoMfk8e

## Contributing

Please feel free to open an issue for any suggestions.

### Credit and thanks to:

* <https://www.coingecko.com/en/api/documentation> CoinGecko API.

