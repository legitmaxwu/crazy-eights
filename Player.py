import pydealer as pd
import names
import time
import random
from utils import SUITS, get_INSTANT_GAMEPLAY

class Player(object):
      
  def drawCards(self, num_cards):
    dealt_cards = self.host_game.giveCards(num_cards)
    self.hand.extend(dealt_cards)
    return

  # add card to discard and remove from hand
  def playCard(self, card):
    if self.isNPC():
      # print("Trying to play {}.".format(card.name))
      print("Trying to play card [{}].".format(self.hand.index(card) + 1))
      if not get_INSTANT_GAMEPLAY():
        time.sleep(1)
    if self.host_game.discardCard(card) == False: # failed to discard card (rules not obeyed)
      return False

    # card has been played, so remove from hand
    if self.isNPC():
      print("... Played {}!".format(card.name))
      if not get_INSTANT_GAMEPLAY():
        time.sleep(1)
    self.hand.remove(card)
    return True

  def __init__(self, host_game):

    self.host_game = host_game
    self.hand = []
    self.name = None


class Person(Player):

  # ask person what they want to do
  def makeMove(self):
    
    # if you own a playable card, you must play it
    can_play = False
    for card in self.hand:
      if self.host_game.canDiscard(card):
        can_play = True

    choice = input("Which card do you want to play? ")
    # make sure input is valid
    while not choice.isnumeric() or int(choice) <= 0 or (int(choice) > len(self.hand)):
      if choice.isnumeric() and int(choice) == 999:
        if can_play:
          print("... Sorry, you have a playable card and must play it!")
        else:
          Player.drawCards(self, 1)
          return True
      print("Please choose a valid card (number between 1 and {})".format(len(self.hand)))
      print("Input 999 to draw a card and skip your turn")
      choice = input("Which card do you want to play? ")

    # select card and play it
    choice = int(choice)
    choice -= 1
    card = self.hand[choice]
    if Player.playCard(self, card) == False:
      print(card.name, "cannot be played.")
      return False
    return True

  def chooseSuit(self):
    choice = input("You played a 'crazy' card! Choose a suit for the next player:\n'Clubs', 'Diamonds', 'Hearts', or 'Spades'. ")
    while choice not in SUITS:
      print("Please choose a valid suit.")
      choice = input("Choose a suit for the next player: ")
    return choice

  def promptName(self):
    self.name = input("Enter a name: ")
    print("Player created with name", self.name)
    return

  def isNPC(self):
    return False
    
  def __init__(self, host_game):
    Player.__init__(self, host_game)
    self.promptName()

class NPC(Player):
  
  def isNPC(self):
    return True

  # select card to play (NPC)
  def makeMove(self):
    # select card
    selection = 0
    while Player.playCard(self, self.hand[selection]) == False:
      # print("{} cannot be played.".format(self.hand[selection].name))
      print("... Card [{}] cannot be played.".format(selection + 1))
      selection += 1
      if not get_INSTANT_GAMEPLAY():
        time.sleep(0.3)
      if selection >= len(self.hand):
        print("I guess none of my cards can be played. Let's draw a card!")
        Player.drawCards(self, 1)
        if not get_INSTANT_GAMEPLAY():
          time.sleep(1)
        return True

  def chooseSuit(self):
    print("Played a 'crazy' card! Choosing a suit... ")
    if not get_INSTANT_GAMEPLAY():
      time.sleep(1)
    return(random.choice(SUITS))

  def __init__(self, host_game):
    Player.__init__(self, host_game)
    self.name = names.get_first_name()
    
    