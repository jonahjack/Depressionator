from twitchio.ext import commands
import sys
sys.path.insert(0, "../")
import Vars

badwords = []
badWords = open('BannedWords.txt', 'r')
for line in badWords.readlines():
    line = line.strip()
    badwords.append(line)

class Bot(commands.Bot):

    def __init__(self):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        # prefix can be a callable, which returns a list of strings or a string...
        # initial_channels can also be a callable which returns a list of strings...
        super().__init__(token=Vars.token, prefix=Vars.prefix, initial_channels=[Vars.channel])

    async def event_ready(self):
        # Notify us when everything is ready!
        # We are logged in and ready to chat and use commands...
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    async def event_message(self, message):
        # Messages with echo set to True are messages sent by the bot...
        # For now we just want to ignore them...
        if message.echo:
            return

        # Print the contents of our message to console...
        print(message.content)

        # Since we have commands and are overriding the default `event_message`
        # We must let the bot know we want to handle and invoke our commands...
        await self.handle_commands(message)

    @commands.command()
    async def hello(self, ctx: commands.Context):
        # Here we have a command hello, we can invoke our command with our prefix and command name
        # e.g ?hello
        # We can also give our commands aliases (different names) to invoke with.

        # Send a hello back!
        # Sending a reply back to the channel is easy... Below is an example.
        await ctx.send(f'Hello {ctx.author.name}!')
    @commands.command()
    async def trigger(self, ctx: commands.Context, message):
        await ctx.send(f'Hello {ctx.author.name} and thank you for the trigger word submission, your answer is being evaluated and will be added shortly. Keep in mind it has been added to a list and will be chosen at random')
        lowerMessage = message.lower()
        res = any(ele in lowerMessage for ele in badwords)
        if res != True:
            with open("TriggerWords.txt","a") as file:
                file.write(message + "\n")
                file.close()
    @commands.command()
    async def insult(self, ctx: commands.Context, message):
        await ctx.send(f'Hello {ctx.author.name} and thank you for the Insult submission, your answer is being evaluated and will be added shortly. Keep in mind it has been added to a list and will be chosen at random')
        lowerMessage = message.lower()
        res = any(ele in lowerMessage for ele in badwords)
        if res != True:
            print(message)
            with open("Insults.txt","a") as file:
                file.write(message + "\n")
                file.close()
        
        


bot = Bot()
bot.run()
# bot.run() is blocking and will stop execution of any below code here until stopped or closed.