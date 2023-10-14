import discord
import os

### Class
class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user}')
        await self.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you")) 

    async def on_message(self, message):
        print(f'Received message from {message.author}: {message.content}')

        # preventing the bot to answer so himself
        if message.author == self.user:
            return
        
        if message.content.startswith('$hello'):
            await message.channel.send('Hello!')

### Intents
intents = discord.Intents.default()
intents.message_content = True

### Client
client = MyClient(intents=intents)

### store token in token.txt
# please do not store your token here.
# This bot will only ask you for the token if there is none set.
# After initialising it the first time with the token it will permanently be saved in the token.txt
# Therefore please ensure to check the .gitignore to contain an entry for token.txt for the safety of your bot.
token = ""
tokenPath = 'token.txt'
if os.path.exists(tokenPath):
    # get token from token.txt
    with open(tokenPath, 'r') as file:
        token = file.read().replace('\n', '')
else:
    # set token
    token = input("There is no token saved yet. Please provide the Token for your Discord bot:")
    with open(tokenPath, 'w') as file:
        file.write(token)
client.run(token)
