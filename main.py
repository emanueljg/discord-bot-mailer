from typing import Sequence
import discord
from discord import channel
from discord.ext import commands
#from datetime import timezone, timedelta
from config import TOKEN

from discord.member import Member
from lib import send_mail

intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix='dbm ', intents=intents)

#CEST = timezone(offset=timedelta(hours=2))

def trunc(seq: Sequence, max_length=50):
    return seq if len(seq) <= max_length else seq[:max_length-3] + '...'

#def get_message_time(message: discord.Message, format='%Y-%m-%d %H:%M:%S', tz=CEST):
#    return message.created_at.astimezone(tz=tz).strftime(format)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.event
async def on_message(message: discord.Message):
    if isinstance(message.channel, discord.DMChannel):
        send_mail(
            subject=f'[DM/{message.author}] {trunc(message.content)}',
            body=message.content
            #body=f'({get_message_time(message)})\n\n{trunc(message.content)}'
        )
    else:
        author = message.author.nick or str(message.author)
        send_mail(
            subject=f'[{message.guild}/{message.channel}] ({author}) {trunc(message.content)}',
            body=message.content
            #body=f'({get_message_time(message)}) {author}\n\n{message.content}'
    )

bot.run(TOKEN)