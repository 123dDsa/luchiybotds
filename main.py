import disnake
from disnake.ext import commands
import random
from encoder import Decoder
from cmds import Cmd
from encoder import Reg

bot = commands.Bot(command_prefix="!",help_command=None, intents=disnake.Intents.all())

#"+exec>help" - > "+exec",">","help" < command[2]


guild = None
@bot.event
async def on_ready():
    global guild
    print("Бот запущен и готов к работе")
    channel = bot.get_channel(1213234754967576586)
    embed = disnake.Embed(title=f"{bot.user.name} | Информация о работе бота", description=f"**{bot.user.name}** запущен!\nПинг: **{round(bot.latency * 1000)}**мс\nБот загрузил **{len(bot.commands)}** команд")
    await channel.send(embed=embed)
    await bot.change_presence(status = disnake.Status.idle, activity = disnake.Game("!help"))

    guild = bot.get_guild(1213226246876700702)
#wsadmlas -> da


@bot.event
async def on_message(message):
    if message.author.bot:
        return
    
    cmd = Cmd()
    command = cmd.Decode(message.content)

    if command["Cmd"] == "$stats":
        decode = Decoder("test.test")
        data = decode.Decode()
        print(data)
        text = {}
        for token in data:
           text[token["user"]] = f"Money: {str(token["stats"]["money"])}, Diamonds: {str(token["stats"]["diamons"])}, Name: {str(token["stats"]["name"])}"
        
        await message.channel.send(text[command["Args"][0][1]])
    elif command["Cmd"] == "$register":
        if command["Args"] == None:
            decode = Decoder("test.test")
            data = decode.Decode()
            print(data)
            for token in data:
                if str(message.author.id) == token["user"]:
                    await message.channel.send("У вас уже есть статистика!")
                    return

            reg = Reg()
            reg.register(str(message.author.id),message.author.name)
            await message.channel.send("Вы успешно зарегестрировались!")
        else:
            decode = Decoder("test.test")
            data = decode.Decode()
            print(data)
            for token in data:
                for arg in command["Args"]:
                    if arg[0] == "id":
                        if arg[1] == token["user"]:
                            await message.channel.send(f"У {arg[1]} уже есть статистика!")
                            return
            reg = Reg()
            for arg in command["Args"]:
                if arg[0] == "id":
                    reg.register(arg[1],guild.get_member(int(arg[1])).name)
                    await message.channel.send(f"Вы успешно зарегестрировали {arg[1]}!")

# @bot.command()
# async def stats(ctx):
#     decode = Decoder("test.test")
#     data = decode.Decode()
#     print(data)
#     text = {}
#     for token in data:
#         text[token["user"]] = f"Money: {token["user"]["stats"]["money"]}, Diamonds: {token["user"]["stats"]["diamonds"]}"
#     await ctx.send()

# @bot.command()
# async def ping(ctx):
#     await ctx.send("pong")

# # ---------------------------------------------------
# # TAK NADO
# # online_count = sum(1 for member in guild.members if not member.bot if member.status == disnake.Status.online or member.status == disnake.Status.dnd)
# # ---------------------------------------------------
    
# @bot.command()
# async def gif(ctx):
#     with open('gifs.txt', 'r') as file:
#         links = file.readlines()
#     random_link = random.choice(links).strip()
#     await ctx.send(random_link)



bot.run("MTIxMzIyNTIxMjc3OTMwNzA2OQ.GuN7t3.9xY4A74FF9VUukWHI4A92OTcZeFkw9K-B8IpkU")
#PEREMOGAAAAA