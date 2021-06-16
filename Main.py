import discord

client = discord.Client()

@client.event
async def on_ready():
	await client.change_presence(activity=discord.Game(''))

	print ('We have logged in as {0.user}'.format(client))
  
  client.run('')
