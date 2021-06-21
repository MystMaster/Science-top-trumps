#!/bin/python3
from animal import animals
from time import *
import random

print("Welcome to my science project. Here you can learn about chemical elements in a fun way! Try to beat the computer with ")
sleep(1)
while True:
  print('Do you want to play the chemical elements top trump game? Type "b" to begin. ')
  category = input(">")
  categories = ["e", "other"]
  while category not in categories:
    print('Please enter either "e" or "other"')
    category = input(">")
  print("")
  print("Here is the list of cards: ")
  sleep(1)

  if category == "e":
    cards = animals
  else:
    cards = planets
  for c in cards:
    print(c.name)

  sleep(1)
  user = random.choice(cards)
  bot = random.choice(cards)

  print("")
  print("Your card is ... {}.".format(user.name))
  sleep(1)
  print("")
  print("Computer's card is a secret!")
  print("")

  sleep(1)
  print("Choose a topic to play against the computer: ", ", ".join(user.options))

  answer = input(">")
  sleep(1)
  print("Comparing {}...".format(answer))
  sleep(1)

  def compare(a, b):
    if a > b:
      sleep(1)
      print("")
      print("You win!")
      sleep(1)
      print("Computer's card was...{}.".format(bot.name))
      sleep(1)
      print("The {} of {} is {}.".format(answer, user.name, a))
      sleep(1)
      print("The {} of {} is {}.".format(answer, bot.name, b))

    
    elif a == b:
      sleep(1)
      print("")
      print("Tie!")
      print("Computer's card was...{}.".format(bot.name))
      sleep(1)
      print("The {} of {} is {}.".format(answer, user.name, a))
      sleep(1)
      print("The {} of {} is {}.".format(answer, bot.name, b))
      
    else:
      sleep(1)
      print("")
      print("Computer wins!")
      sleep(1)
      print("Computer's card was...{}.".format(bot.name))
      sleep(1)
      print("The {} of {} is {}.".format(answer, user.name, a))
      sleep(1)
      print("The {} of {} is {}.".format(answer, bot.name, b))
      
  if answer == "atomic_weight":
    compare(user.atomic_weight, bot.atomic_weight)
    
  elif answer == "group":
    compare(user.group, bot.group)
    
  elif answer == "period":
    compare(user.period, bot.period)
    
  elif answer == "density":
    compare(user.density, bot.density)
    
  elif answer == "melting_point":
    compare(user.melting_point, bot.melting_point)

 
  else:
    print("Invalid imput.")
  
  sleep(1)
  player = input("Do you want to play another round? y/n ")

  if player == "y" or player == "yes":
    print("")
    sleep(1)
    
  elif player == "n" or player == "no":
    print("Okay then.")
    break

  else:
    print("Invalid input.")
    break