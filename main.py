"""
Start a Crazy Eights game.

Usage: arguments_example.py [-h] [-p NUM_PLAYERS] [-n NUM_NPCS] [-r RULES_FILE] [-i]

Options:
  -h --help
  -p --people NUM_PEOPLE      Number of players
  -n --npcs NUM_NPCS          Number of NPC's
  -r --rules RULES_FILE       File containing rules config
  -i --instant                Do not show NPC decision-making
"""

from docopt import docopt
from CrazyEightsGame import CrazyEightsGame
from utils import set_INSTANT_GAMEPLAY


def main():
  arguments = docopt(__doc__)
  if arguments['--instant']:
    set_INSTANT_GAMEPLAY(True)
  game = CrazyEightsGame(arguments)

if __name__ == '__main__':
  main()
