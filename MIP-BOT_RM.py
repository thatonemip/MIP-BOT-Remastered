#please note: This A.I/Chatbot does not use Chatterbot.
#Loads in all the imports "needed" to run MIP-BOT RM
print("Loading some things. . .")
import os
print("Loaded 'os'")
import itertools
print("Loaded 'itertools'")
import threading
print("Loaded 'threading'")
import time
print("Loaded 'time'")
import sys
print("Loaded 'sys'")
import csv
print("Loaded 'csv'")
import random
print("Loaded 'random'")
time.sleep(1)
print("Loaded all imports")
from os import system, name
from datetime import datetime
from time import sleep

#Def's the "screen_clear" function to clear the screen
def screen_clear():
   if name == 'nt':
      _ = system('cls')
   else:
      _ = system('clear')
sleep(2)

def getnamewhat():
  print("Hello there", username, "type something")
  print("to speak to me")

#Name screen
screen_clear()
print("=====================================")
print()
print()
print("             MIPWARE.INC")
print("              2022-2023 ")
print()
print()
print("              MIP-BOT")
print()
print("=====================================")
time.sleep(2)
screen_clear
print("DISCLAMER!!!")
print()
print("this python A.I is very buggy!")
time.sleep(2)
screen_clear()

#Asks for the users name
print("What is your name?")
username = input("Name: ")
print("Hello there", username)
time.sleep(1.5)
screen_clear()


#Lots of info is shown on the screen here
print("This is MIP-BOT")
print("Prototype Version: (no longer an prototype)")
print("Version: 0.0.6 beta")
print("Programmed by: Isaac D aka 'Therealmip'")
print()
print("NOTE: This AI chatbot origanally from:")
print("Isaac D aka 'Therealmip'")
print("Remember: commands start with an '!'")
print("Do '!Help' to open the help ui")
print("If you want to leave the software say 'exit'")
print("===============================================")
print()
print()
getnamewhat()
print()
print()

#Def's the part where you can talk to the A.I/Chatbot
#or what i like to call it, the "say" function
def saysomethingpan():
  saywhat1 = input("Say: ")

  if saywhat1 == ("hello"):
    print ("Greetings", username)
    saysomethingpan()

  elif saywhat1 == ("hi"):
    print("Greetings", username)
    saysomethingpan()

  elif saywhat1 == ("greetings"):
    print("Greetings", username)
    saysomethingpan()

  elif saywhat1 == ("hello there"):
    print("Greetings", username)
    saysomethingpan()

  #Runs an function that spams 'YOUR COMPUTER HAS AN VIRUS'
  elif saywhat1 == ("chaos"):
    print("Ah, so you want me to cause chaos right now?")
    time.sleep(1)
    print("Loading 'chaos'. . . ")
    time.sleep(3)
    print("Running 'mip-bot spammer.exe' in...")
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    def spammerwhat():
      time.sleep(0.2)
      print("YOUR COMPUTER HAS AN VIRUS!")
      spammerwhat()
    
    spammerwhat()

  #Runs the function 'MW-CE'
  elif saywhat1 == ("!MW-CE"):
    screen_clear()
    version = ("ver 0.0.4")
    def infoofmwce():
      print("MIPWARE Command Executor (MW-CE)")
      print("Copyright 2021-2022")
      print(version)
      print()
      print()
      print()
      print()
      print()
      print()
      print()
      print()
      print()
      print()
      print()
      print()
      print()
      print()
      print()
      print()
      print()
      print()
      def dosmainmenu():
        command = input("Command: ")
        #commands
        if command == ("help"):
          print()
          print("help: opens an list of commands")
          print("clear: Clears the screen")
          print("exit: Exits the MW-CE")
          print("print: Prints text on the screen")
          print("info: shows the bulid, version and info of MW-CE")
          print("list: Shows external files that can be runned")
          print("run (file name): runs the file that is listed in the command")
          print()
          dosmainmenu()

        elif command == ("clear"):
          screen_clear()
          dosmainmenu()

        elif command == ("list"):
          print()
          print("========files========")
          print()
          print("Coming soon!")
          print()
          dosmainmenu()

        elif command == ("run spammer.exe"):
          print("WARNING: This will spam text on your screen")
          print("Are you sure you want to run this program?")
          commandwhat1 = input("y? n?: ")
          
          if commandwhat1 == ("y"):
            print("Running 'spammer.exe'...")
            def spammerwhat4():
              time.sleep(0.2)
              print("YOUR COMPUTER HAS AN VIRUS!")
              spammerwhat4()
            spammerwhat4()

          

          elif commandwhat1 == ("n"):
            print("Aborting")
            dosmainmenu()

          else:
            print("Invalid choice")
            dosmainmenu()



        elif command == ("exit"):
          screen_clear()
          saysomethingpan()

        elif command == ("print"):
          GYTVTRCT = input("Enter text to print: ")
          print(GYTVTRCT)
          dosmainmenu()

        elif command == ("time"):
          now = datetime.now()
          current_time = now.strftime("%H:%M:%S")
          print("The current time is", current_time)
          dosmainmenu()
        
        #File reading system template
        elif command == (" run File name here"):
          exec(open('File name here').read())
          dosmainmenu()


        elif command == ("info"):
          infoofmwce()
          dosmainmenu()

        elif command == ("easteregg1"):
          print("Android is better then IOS, change my mind")
          dosmainmenu()

        else:
          print("ERROR 001: Invlid command")
          dosmainmenu()

      dosmainmenu()
    infoofmwce()



  elif saywhat1 == ("what do you hate"):
    print("I hate computer virus's")
    saysomethingpan()

  elif saywhat1 == ("what does chaos mean"):
    print("Chaos")
    print()
    print("noun:")
    print("complete disorder and confusion.")
    print()
    print("in Physics:")
    print("behavior so unpredictable as to appear random, owing to great sensitivity to small changes in conditions.")
    print()
    saysomethingpan()

  elif saywhat1 == ("exit"):
    print("Exiting software. . .")
    time.sleep(2)
    exit

  elif saywhat1 == ("what is my name"):
    print("Your name is", username)
    saysomethingpan()

  elif saywhat1 == ("who am i"):
    print("You are", username)
    saysomethingpan()

  elif saywhat1 == ("test"):
    print("This is an test")
    print("Hello there")
    print("can you read this")
    print()
    print("TEST, TEST")
    saysomethingpan()

  elif saywhat1 == ("!clear"):
    screen_clear()
    saysomethingpan()

  elif saywhat1 == ("do you hate me"):
    print("No, i do not hate you or anyone :)")
    saysomethingpan()

  elif saywhat1 == ("When was you programmed"):
    print("I was made/programmed somethime near Dec 8 2021")
    saysomethingpan()

  elif saywhat1 == ("who are you"):
    print("I am the newer ver of MIP-BOT")
    saysomethingpan()

  elif saywhat1 == ("what time is it"):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("The current time is", current_time)
    saysomethingpan()

  elif saywhat1 == ("!debug"):
    print("Coming soon!")
    saysomethingpan()

  elif saywhat1 == ("!help"):
    print()
    print("!help -Opens the help ui")
    print("!clear -Clears the screen")
    print("!debug -Coming soon!")
    print("!MW-CE -Starts MW-CE")
    print()
    saysomethingpan()

  elif saywhat1 == ("what"):
    print("Wait, what? :/")
    saysomethingpan()

  elif saywhat1 == ("say"):
    print("What do you want me to say?")
    saythingwhat1 = input("Say: ")
    print(saythingwhat1)
    saysomethingpan()

  elif saywhat1 == ("who is Therealmip"):
    print("'Therealmip' is Isaac D, he programmed me")
    saysomethingpan()

  elif saywhat1 == ("what is the time"):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("The current time is", current_time)
    saysomethingpan()

  elif saywhat1 == ("who is Isaac D"):
    print("Isaac D is 'Therealmip', he programmed me")
    saysomethingpan()

  elif saywhat1 == ("what is your fav vid"):
    print("I do not have an fav vid due to me being an chat bot")
    saysomethingpan()

  elif saywhat1 == ("who made you"):
    print("I was programmed by Isaac D")

  elif saywhat1 == ("yeah"):
    print("Mhm")
    saysomethingpan()

  elif saywhat1 == ("what does api mean"):
    print()
    print("Application programming interface")
    print()
    saysomethingpan()

  elif saywhat1 == ("what does ide mean"):
    print()
    print("Integrated development environment")
    print()
    saysomethingpan()

  elif saywhat1 == ("what is a ide"):
    print()
    print("Integrated development environment")
    print()
    print("An integrated development environment is a software application that provides comprehensive facilities to computer programmers for software development. An IDE normally consists of at least a source code editor, build automation tools and a debugger.")
    print()
    saysomethingpan()  

  elif saywhat1 == ("what is a api"):
    print()
    print("Application programming interface")
    print()
    print("An application programming interface is a connection between computers or between computer programs. It is a type of software interface, offering a service to other pieces of software. A document or standard that describes how to build or use such a connection or interface is called an API specification")
    print()
    saysomethingpan()

  elif saywhat1 == ("how are you"):
    print("I am doing fine today, how about you", username)
    howaboutu = input("good, fine, bad: ")

    if howaboutu == ("good"):
      print("Thats nice")
      usermood = ("Doing good")
      saysomethingpan()

    elif howaboutu == ("bad"):
      print("aw man, i hope you feel better soon")
      usermood = ("Bad")
      saysomethingpan()

    elif howaboutu == ("fine"):
      print("Thats good, im glad your feeling aright on this fine day")
      usermood = ("Fine")
      saysomethingpan()

    else:
      print("Error")
      usermood = ("Error")
      saysomethingpan()


  else:
    print("I dont know that")
    saysomethingpan()

#Runs the "say" function that we defed
saysomethingpan()
