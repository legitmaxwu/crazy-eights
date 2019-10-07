# crazy-eights
Crazy Eights, with customizeable rules!

### Usage

First, install Python 3.6.8. Then, run these commands:

```
pip install -r requirements.txt
```

See the help menu using this command:

```
python ./main.py -h
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

