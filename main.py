import discord
from discord.ext import commands
import os


client = commands.Bot(command_prefix = ".")
client.remove_command("help")


@client.event
async def on_ready():
  print('Запущен бот {0.user}'.format(client))
  await client.change_presence(status = discord.Status.online, activity = discord.Game("Kelsi"))

#embed
@client.command()
@commands.has_role(857712477400072234)
async def message(ctx):
  embed = discord.Embed(title = "Что за цифры рядом с ролью?", description = "У нас есть несколько ролей \n \n ・Гость [0+] - Эта роль даётся абсолютно всем при входе на сервер \n ・Обитатель [10+] - Эта роль выдаётся при достижении 10+ уровня \n ・Опытный обитатель [20+] - Эта роль выдаётся при достижении 20+ уровня \n ・Мастер [30+] - Эта роль выдаётся при достижении 30+ уровня. \n \n **Как вы уже могли понять, цифры в квадратных кавычках означают уровень.** \n *А как же качать уровень?* Уровень качается за счёт общения", color = 0x99ddff)
  embed.set_thumbnail(url=ctx.guild.icon_url)
  await ctx.send(embed=embed)
  

    
#help
@client.command()
async def help(ctx, module: str = None):
  if module == 'clear':
    embed = discord.Embed(title = "Команда .help clear", color = 0x2f3136, description = "Очистить сообщения в чате.")
    embed.add_field(name = "Основная информация", value = "Использование: `.clear <количество>`", inline = False)
    embed.add_field(name = "Пример №1", value = "`.clear 5`\n Очистит 5 возможных сообщений в чате", inline = False)
    embed.add_field(name = "Пример №2", value = "`.clear 100`\n Очистит 100 возможных сообщений в чате", inline = False)
    embed.add_field(name = ":warning: Модераия", value = "Это команда модерации, доступная участникам сервера лишь при наличии определённой роли")
    embed.set_thumbnail(url=ctx.guild.icon_url)
    await ctx.send(embed=embed)
  else:
    embed = discord.Embed(title = "Краткая информация о боте", description = "**Kelsi bot** был создан специально для дискорд сервера Kelsi's community \n \n Сейчас в этом боте очень мало функций и он в активной разработке. Для обычных пользователей команд в данный момент нету", color = 0x99ddff)
    embed.set_thumbnail(url=ctx.guild.icon_url)
    await ctx.send(embed=embed)

#Очистка
@client.command()
async def clear(ctx, count: int = None):
    if count:
      await ctx.channel.purge(limit=count+1)
      await ctx.send(f"Было удаленно {count} сообщений")
    else:
      await ctx.send("Пожалуйста, введите количество удаляемых сообщений\n подробнее в .help clear")

#кик
@client.command()
async def kick(ctx, member: discord.Member = None, *, reason:str =None):
    if member:
        if reason:
            await member.kick(reason=reason)
            await ctx.send(embed=discord.Embed(description=f'Пользователь {member.mention} был кикнут \nПричина: {reason}' ))
        else:
            await member.kick()
            await ctx.send(embed=discord.Embed(description=f'Пользователь {member.mention} был кикнут'))
    else: 
        await ctx.send('Введите имя пользователя')

token = os.environ['token']
client.run(token)