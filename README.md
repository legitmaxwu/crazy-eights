# crazy-eights

Crazy Eights, with customizeable rules!

### Usage

First, install Python 3.6.8. Then, run these commands:

```
pip install -r requirements.txt
```

See the help menu using this command:

```
python main.py -h
```

To start a game with 1 player, 3 NPCs, and using `rules.txt` to specify rules, run:

```
python main.py -p 1 -n 3 -r rules.txt
```

Find more advanced usage guidelines below **Rules.**

### Rules

[Crazy Eights](https://vipspades.com/crazy-eights-rules/) is a very simple card game, similar to Uno. Players start with 5 cards and take turns placing cards into a central pile. The card you place must satisfy one of two criteria:

- Match the **suit** (Clubs, Diamonds, Hearts, Spades) of the pile's top card.
- Match the **rank** (Ace to King) of the pile's top card.

There are some special cards in this game:

- **Reverse:** When played, the order of play is reversed.
- **Skip:** When played, the next player is skipped.
- **Crazy 8:** This card may be placed on top of any card. When you play it, you can specify a suit, and the next player must obey this suit.

### Advanced Usage

##### Customizing `rules.txt`

The format per line for `rules.txt` goes as such:

```
[RANK] of [SUIT]: [effect1], [effect2], [effect3]
```

For example,

```
10 of Clubs: wild, reverse, skip
```

would make the 10 of Clubs a wild, reverse, and skip card.

- The ranks are: Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King
- The suits are: Clubs, Diamonds, Hearts, Spades

### Credits

Modules used are listed in `requirements.txt`. Code pulled from outside sources is linked appropriately.

