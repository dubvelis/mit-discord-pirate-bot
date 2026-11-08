"""First Discord connection test for the MIT assignment."""
import os

import discord
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("TOKEN")
if not token:
    raise SystemExit("Add your Discord bot token as TOKEN in the .env file.")

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"Connected to Discord as {client.user}.")


@client.event
async def on_message(message):
    if not message.author.bot and message.content.strip() == "$hello":
        await message.channel.send("Hello!")


client.run(token)
