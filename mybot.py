"""A simple pirate-themed Discord bot using OpenRouter."""
import asyncio
import os

import discord
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
token = os.getenv("TOKEN")
key = os.getenv("OPENROUTER_KEY")
if not token or not key:
    raise SystemExit("Add TOKEN and OPENROUTER_KEY to your .env file.")

ai = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=key)
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


def pirate_answer(question):
    result = ai.chat.completions.create(
        model="openrouter/free",
        messages=[
            {"role": "system", "content": "Answer helpfully and briefly in the friendly voice of a pirate."},
            {"role": "user", "content": question},
        ],
        max_tokens=400,
    )
    return result.choices[0].message.content or "Arrr, I couldn't find an answer."


@client.event
async def on_ready():
    print(f"Connected to Discord as {client.user}.")


@client.event
async def on_message(message):
    if message.author.bot:
        return
    content = message.content.strip()
    if content == "$hello":
        await message.channel.send("Hello!")
    elif content == "$question" or content.startswith("$question "):
        question = content[len("$question"):].strip()
        if not question:
            await message.channel.send("Ask me something after $question, matey!")
            return
        try:
            async with message.channel.typing():
                answer = await asyncio.to_thread(pirate_answer, question)
            await message.channel.send(answer[:1900], allowed_mentions=discord.AllowedMentions.none())
        except Exception:
            await message.channel.send("Arrr, I couldn't answer just now. Please try again later.")


client.run(token)
