from discord.ext.commands import Bot
import asyncio
import time

Client = discord.Client ()
client = commands.Bot (command_prefix = "+")


@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="+help | By MegaPig"))
    print("Bot Is Ready")

   
@client.event
async def on_message(message):
    if message.content.startswith('+hello'):
        await client.send_message(message.channel, """`Hello! Im MegaBot`
**My Creator Is MegaPig!**""")
    if message.content.startswith('+invite'):
        await client.send_message(message.channel, "https://discordapp.com/api/oauth2/authorize?client_id=459490391146627073&permissions=8&scope=bot __You Can Invite Me All Days!__                                                **MegaPig#1576** Is My Creator!")

    if message.content.startswith('+help'):
        embed = discord.Embed(title="Command List", description="""
__**Information Commands**__

+hello
+invite

__**Music Command**__

+join""", color=0xe88af4)
        await client.send_message(message.channel, embed=embed)

                                
Client.run(process.env.BOT_TOKEN);
