import pydealer as pd
import cowsay
from Player import Player, NPC, Person
import random
from utils import printCards, printRect, printBlanks, SUITS, RANKS, EFFECTS, get_INSTANT_GAMEPLAY
import os
import time
import art
import textwrap

class CrazyEightsGame(object):
  
  """
  Rules:
    crazy: after card is placed, player can specify a suit for the next player.
    wild: can be placed on top of any card
  """

  # remove cards from deck and return
  def giveCards(self, num_cards):
    return self.deck.deal(num_cards)

  def canDiscard(self, card_played):
    top_card = None
    if len(self.discard) > 0:
      top_card = self.discard[-1]

    if top_card == None or card_played == None:
      return True
    if self.crazy and card_played.suit == self.crazy_suit:
      return True
    if top_card.value == card_played.value:
      return True
    if top_card.suit == card_played.suit:
      return True

    # check wild cards
    if any(card == card_played for card in self.rules['wild']):
      return True

    return False

  # add card to discard pile
  def discardCard(self, card):
    if self.canDiscard(card) == False:
      return False

    self.discard.add(card)
    return True
  
  """
  Print player turns
  """
  def printTurn(self, curr_player):
    # Print stuff
    os.system('cls' if os.name == 'nt' else 'clear')
    if curr_player.isNPC() == False or True:

      # print game information
      print("Game Information")
      print("--------------------------------------------------")
      print(" ", "{:<12} {:<3}".format("Player", "Cards Left"))
      for player in self.players:
        if player == curr_player:
          print(">", "{:<12} {:<3}".format(player.name, len(player.hand)))
        else:
          print(" ", "{:<12} {:<3}".format(player.name, len(player.hand)))
      print()
      print()
      print("{}'s turn!".format(curr_player.name))
      print("--------------------------------------------------")
      print()

      # print discard pile
      print("Pile:")
      if len(self.discard) > 0:
        printCards([self.discard[-1]], False)
      else:
        printRect()

      # print player's hand
      print()
      print("{}'s Hand:".format(curr_player.name))
      if curr_player.isNPC():
        printBlanks(curr_player.hand)
      else:
        printCards(curr_player.hand)
      print()

      if self.crazy:
        print("Note: Last card played was a crazy card! The suit is {}.".format(self.crazy_suit))
        print()

  """
  Cycles through players, who make moves until there is a winner.
  """
  def gameLoop(self):
    
    # randomize order of players
    random.shuffle(self.players)
    curr_player_index = 0
    iterator = 1

    while True:
      curr_player = self.players[curr_player_index]

      # spoiler alert
      if not curr_player.isNPC():
        os.system('cls' if os.name == 'nt' else 'clear')        
        cowsay.cow("It is {}'s turn! Press [Enter] to continue.".format(curr_player.name))
        dummy = input()
      
      # print screen
      self.printTurn(curr_player)

      # make move
      while curr_player.makeMove() == False:
        if curr_player.isNPC() == False:
          print("... Make another move! Consider typing '999' to draw a card")

      # check for special effects
      self.crazy = False
      if len(self.discard) > 0:
        top_card = self.discard[-1]
        if 'crazy' in self.rules and top_card in self.rules['crazy']:
          chosen_suit = curr_player.chooseSuit()
          self.crazy = True
          self.crazy_suit = chosen_suit
          os.system('cls' if os.name == 'nt' else 'clear')
          cowsay.cow("CRAAAZY CARD! The suit is {}!".format(self.crazy_suit))
          input("Press [Enter] to continue...")
        if 'reverse' in self.rules and top_card in self.rules['reverse']:
          iterator -= 1
        if 'skip' in self.rules and top_card in self.rules['skip']:
          curr_player_index += iterator

      # check for empty deck
      if len(self.deck) <= 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        cowsay.cow("Deck is empty. \nShuffling the discard pile back into the deck!")
        all_but_top = self.discard[:-1]
        self.discard = [self.discard[-1]]
        self.deck = all_but_top
        if not get_INSTANT_GAMEPLAY():
          time.sleep(3)

      # check for winner
      if len(curr_player.hand) == 0:
        print("WE HAVE A WINNER:", curr_player.name)
        break

      curr_player_index += iterator
      num_players = len(self.players)
      if curr_player_index >= num_players:
        curr_player_index = curr_player_index % num_players
      if curr_player_index < 0:
        curr_player_index = curr_player_index % num_players

    return

  def printRule(self, rule):
    rule_id = rule.lower()
    if rule_id not in self.rules:
      return
    print("'{}' cards:".format(rule))
    print('...', ', '.join([card.name for card in self.rules[rule_id]]))

  def readRules(self, rules_file):

    lines = [line.rstrip('\n') for line in open(rules_file)]
    line_number = 1

    for line in lines:

      line = [term.strip(' ') for term in line.split(':')]
      card = line[0].split(' of ')
      card_rank = card[0]
      card_suit = card[1]

      if card_rank not in RANKS:
        exit("ERROR: `{}`, line {} -- {} is not a valid card rank.".format(rules_file, line_number, card_rank))
      if card_suit not in SUITS:
        exit("ERROR: `{}`, line {} -- {} is not a valid card suit.".format(rules_file, line_number, card_suit))

      effects = [effect.strip(' ') for effect in line[1].split(',')]
      for effect in effects:
        if effect not in EFFECTS:
          exit("ERROR: `{}`, line {} -- {} is not a valid game effect.".format(rules_file, line_number, effect))
        if effect in self.rules:
          self.rules[effect].append(pd.Card(card_rank, card_suit))
        else:
          self.rules[effect] = []
          self.rules[effect].append(pd.Card(card_rank, card_suit))
      line_number += 1

  def initGame(self, args):

    # read rules from rules file
    rules_file = args['--rules']
    self.readRules(rules_file)

    # make players
    num_people = args['--people']
    num_npcs = args['--npcs']

    # print welcome screen
    os.system('cls' if os.name == 'nt' else 'clear')
    print(art.text2art("Crazy Eights", chr_ignore=True))
    print("Welcome to Crazy Eights!")
    
    print("Rules -- specified from `{}`".format(rules_file))
    for effect in EFFECTS:
      self.printRule(effect)

    # make people
    if num_people:
      for i in range(int(num_people)):
        self.players.append(Person(self))

    # make NPCs
    if num_npcs:
      for i in range(int(num_npcs)):
        self.players.append(NPC(self))

    # # of players can't be over 6
    MAX_PLAYERS = 6
    if len(self.players) == 0:
      exit("ERROR: Number of players cannot be 0.")
    if len(self.players) > MAX_PLAYERS:
      exit("ERROR: Cannot have more than {} players.".format(MAX_PLAYERS))

    # init deck and discard pile
    self.deck = pd.Deck()
    self.deck.shuffle()
    self.discard = pd.Deck()
    self.discard.empty() 

    # distribute hands
    NUM_STARTING_CARDS = 5
    for player in self.players:
      player.drawCards(NUM_STARTING_CARDS)
      printCards(player.hand)

    self.gameLoop()

  def __init__(self, args):
  
    self.deck = None        # deck to draw cards from
    self.discard = None     # discard pile
    self.players = []       # players in the game
    self.crazy = False      # has a crazy card just been played?
    self.crazy_suit = None  # chosen suit after crazy card is played
    
    # rules
    self.rules = dict()

    self.initGame(args)