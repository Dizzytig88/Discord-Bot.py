import discord

client = discord.Client()

@client.event
async def on_ready():
	await client.change_presence(activity=discord.Game('#this will make it so your bots status will be playing ____(optional)'))

	print ('We have logged in as {0.user}'.format(client))
  
  client.run('#add your bots token here')
