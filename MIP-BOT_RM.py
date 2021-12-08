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
def screen_clear():
   if name == 'nt':
      _ = system('cls')
   else:
      _ = system('clear')
sleep(2)


def getnamewhat():
  print("Hello there", username, "type something")
  print("to speak to me")

screen_clear()
print("=====================================")
print()
print()
print("             MIPWARE.INC")
print("              2021-2022              ")
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
print("What is your name?")
username = input("Name: ")
print("Hello there", username)
time.sleep(2)
screen_clear()

print("This is MIP-BOT")
print("Prototype Version: (no longer an prototype)")
print("Version: 0.0.3 beta")
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

def saysomethingpan():
  saywhat1 = input("Say: ")

  if saywhat1 == ("hello"):
    print ("Greetings", username)
    saysomethingpan()

  elif saywhat1 == ("exit"):
    print("Exiting software. . .")
    time.sleep(2)
    exit

  elif saywhat1 == ("what is my name"):
    print("Your name is", username)
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

  elif saywhat1 == ("what time is it"):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("The current time is", current_time)
    saysomethingpan()

  elif saywhat1 == ("!help"):
    print()
    print("!help -Opens the help ui")
    print("!clear -Clears the screen")
    print()
    saysomethingpan()

  elif saywhat1 == ("say"):
    print("What do you want me to say?")
    saythingwhat1 = input("Say: ")
    print(saythingwhat1)
    saysomethingpan()

  elif saywhat1 == ("who is Therealmip"):
    print("'Therealmip' is Isaac D, he programmed me")
    saysomethingpan()

  elif saywhat1 == ("who is Isaac D"):
    print("Isaac D is 'Therealmip', he programmed me")
    saysomethingpan()

  elif saywhat1 == ("who made you"):
    print("I was programmed by Isaac D")

  elif saywhat1 == ("yeah"):
    print("Mhm")
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

saysomethingpan()
