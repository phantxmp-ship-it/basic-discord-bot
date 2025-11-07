"""
Basic Discord Bot for Visual Studio
-----------------------------------
To run:
1. Install dependencies:
      pip install discord.py python-dotenv
2. Create a file named .env in the same folder with:
      DISCORD_TOKEN=your_discord_bot_token_here
3. Press F5 or 'Run' in Visual Studio to start the bot.
"""

import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Setup bot intents
intents = discord.Intents.default()
intents.message_content = True

# Create bot instance
bot = commands.Bot(command_prefix="!", intents=intents)

# Event: Bot ready
@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user} (ID: {bot.user.id})")
    print("------")

# Event: Respond to 'hello'
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.lower() == "hello":
        await message.channel.send(f"Hey {message.author.name}! 👋")

    await bot.process_commands(message)

# Command: ping
@bot.command()
async def ping(ctx):
    """Replies with Pong!"""
    await ctx.send("🏓 Pong!") 

# Command: echo
@bot.command()
async def echo(ctx, *, message: str):
    """Repeats your message"""
    await ctx.send(message)

# Run bot
if __name__ == "__main__":
    if not TOKEN:
        print("❌ ERROR: Discord token not found. Add it to your code file.")
    else:
        bot.run(TOKEN)

        