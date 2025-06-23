import os
import emoji
import discord
from discord.ext import commands
import requests

token = os.getenv["BOT_TOKEN"]
channel_id = os.getenv["CHANNEL_ID"]
api_key = os.getenv["API_KEY"]

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
command_list = ["!pocasie", "!cupertino"]
cupertino_pocasie = {}
icon = ""
request = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q=Cupertino&appid={api_key}&units=metric")
data = request.json()
for udaj in data["weather"]:
    cupertino_pocasie.update({"Ako to vyzerá vonku": udaj["main"]})
    icon = udaj["icon"]

for udajj in data["main"]:
    cupertino_pocasie.update({
        "Teplota": f"{data['main']['temp']} °C",
        "Pocitová teplota": f"{data['main']['feels_like']} °C",
        "Minimiálna teplota": f"{data['main']['temp_min']} °C",
        "Maximalna teplota": f"{data['main']['temp_max']} °C",
    })
for udajjj in data["wind"]:
    cupertino_pocasie.update({"Vietor": f"{data['wind']['speed'] * 3.6:.2f} km/h"})



@bot.event
async def on_ready():
    print("Bot sa zapol")
    embed = discord.Embed(
        title=f"Počasie v Cupertine {emoji.emojize(':sunny:')}",
        color=discord.Color.blue()
    )
    embed.set_thumbnail(url=f"https://openweathermap.org/img/wn/{icon}@2x.png")
    for riadok in cupertino_pocasie:
        embed.add_field(name=f"**{riadok}**", value=cupertino_pocasie[riadok], inline=False)
    embed.set_footer(text="datas are fetched from https://openweathermap.org/")
    channel = bot.get_channel(int(channel_id))
    await channel.send(embed=embed)
    await bot.close()
    print("Bot sa vypol")


bot.run(token)
