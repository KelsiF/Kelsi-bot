import discord
from discord.ext import commands

class User(commands.cog):

  def __init__(self, client):
    self.client == client

  @command.cog.listener()
  async def on_ready(self):
    print("ready")

  @commands.command()
  async def info(self, ctx):
    await ctx.send("hello, world!")

def setup(client):
  client.add_cog(User(client))