# Design Document

### Objects

The code is designed to keep the game object and the players object as separate as possible, to optimize for modularity. The only way that players interact with the game is by drawing cards from the game deck, or attempting to play cards into the discard pile. Players do not access direct game data (i.e. the deck, game rules, other players).

##### CrazyEightsGame Object

Contains all the game-related data, including players, rules, and the deck and discard pile. Instead of allowing players to access this data directly, this object uses an API (the `canDiscard()` function, for example) to let players know if their moves are allowed.

##### Player Object

Represents a player in the game. Players have a hand (with cards) and a name. There are 2 types of players inherited: **NPCs** and actual **people**. NPCs and people complete the same actions during the game, but NPCs make automated decisions while people are prompted for their in-game decisions.

### utils.py

This file stores tools unspecific to each game instance--for example, how to print poker cards via ASCII art. It also stores some important global variables.

### Game Logic

Flow for the game:

- Initialize game
- Game loop
  - Player makes move
  - Apply special effects
  - Check for winner
- End game

For a turn-based game, a loop is the best way to capture the repetitive actions during gameplay. A list specifies the order of players, and an index pointer determines whose move it is. The index pointer is guided by an iterator, which determines the order of players moving. This implementation made adding 'reverse' and 'skip' functionalities very easy, as all I had to do was to modify the iterator.

### Tooling

- Python: I used Python because of its ease of use and availability of many library modules. Also, for a simple card game, there are no concerns about performance speed.
- Docopt: I used the Docopt library to handle arguments. It simplifies parsing arguments down to merely typing a detailed comment, cutting development time significantly.
- PyDealer: I chose PyDealer a a very simple and lightweight module for handling card decks. Not having to reimplement the Card and Deck classes saved me a lot of development time.
- Art, Cowsay: These modules helped make the user experience more immersive without me having to spend lots of time carefully creating ASCII art.





