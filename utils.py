SUITS = [
    "Spades", "Clubs", "Diamonds", "Hearts"
]

RANKS = [
    "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"
]

EFFECTS = [
    "wild", "crazy", "skip", "reverse"
]

INSTANT_GAMEPLAY = False

def set_INSTANT_GAMEPLAY(val):
    global INSTANT_GAMEPLAY
    INSTANT_GAMEPLAY = val

def get_INSTANT_GAMEPLAY():
    global INSTANT_GAMEPLAY
    return INSTANT_GAMEPLAY

# Original Code: https://codereview.stackexchange.com/questions/82103/ascii-fication-of-playing-cards

def printBlanks(cards, printIndices=True, return_string=True):
    """
    Instead of a boring text version of the card we render an ASCII image of the card.
    :param cards: One or more card objects
    :param return_string: By default we return the string version of the card, but the dealer hide the 1st card and we
    keep it as a list so that the dealer can add a hidden card in front of the list
    """
    # we will use this to prints the appropriate icons for each card
    suits_name = ['Spades', 'Diamonds', 'Hearts', 'Clubs']
    suits_symbols = ['♠', '♦', '♥', '♣']

    # create an empty list of list, each sublist is a line
    if printIndices == True:
        lines = [[] for i in range(8)]
    else:
        lines = [[] for i in range(7)]

    counter = 0
    display_index = 0
    for card in cards:
        # "King" should be "K" and "10" should still be "10"
        if card.value == '10':  # ten is the only one who's value is 2 char long
            value = card.value
            space = ''  # if we write "10" on the card that line will be 1 char to long
        else:
            value = card.value[0]  # some have a value of 'King' this changes that to a simple 'K' ("King" doesn't fit)
            space = ' '  # no "10", we use a blank space to will the void
        # get the cards suit in two steps
        suit = suits_name.index(card.suit)
        suit = suits_symbols[suit]

        # add the individual card on a line by line basis
        lines[0].append('┌─────────┐')
        lines[1].append('│░░░░░░░░░│')
        lines[2].append('│░░░░░░░░░│')
        lines[3].append('│░░░░░░░░░│')
        lines[4].append('│░░░░░░░░░│')
        lines[5].append('│░░░░░░░░░│')
        lines[6].append('└─────────┘')
        display_index += 1
        if printIndices == True:
            lines[7].append('   [{:>2}]    '.format(display_index))
        
        counter += 1
        if counter == 5:
            result = []
            for index, line in enumerate(lines):
                result.append(''.join(lines[index]))
            print('\n'.join(result))
            if printIndices == True:
                lines = [[] for i in range(8)]
            else:
                lines = [[] for i in range(7)]
            counter = 0
    result = []
    for index, line in enumerate(lines):
        result.append(''.join(lines[index]))
    if counter > 0:
        print('\n'.join(result))

def printRect():
    lines = [[] for i in range(7)]
    lines[0].append('┌─────────┐')
    lines[1].append('│         │')
    lines[2].append('│         │')  
    lines[3].append('│         │')
    lines[4].append('│         │')  
    lines[5].append('│         │')  
    lines[6].append('└─────────┘')
    result = []
    for index, line in enumerate(lines):
        result.append(''.join(lines[index]))
    print('\n'.join(result))


def printCards(cards, printIndices=True, return_string=True):
    """
    Instead of a boring text version of the card we render an ASCII image of the card.
    :param cards: One or more card objects
    :param return_string: By default we return the string version of the card, but the dealer hide the 1st card and we
    keep it as a list so that the dealer can add a hidden card in front of the list
    """
    # we will use this to prints the appropriate icons for each card
    suits_name = ['Spades', 'Diamonds', 'Hearts', 'Clubs']
    suits_symbols = ['♠', '♦', '♥', '♣']

    # create an empty list of list, each sublist is a line
    if printIndices == True:
        lines = [[] for i in range(8)]
    else:
        lines = [[] for i in range(7)]

    counter = 0
    display_index = 0
    for card in cards:
        # "King" should be "K" and "10" should still be "10"
        if card.value == '10':  # ten is the only one who's value is 2 char long
            value = card.value
            space = ''  # if we write "10" on the card that line will be 1 char to long
        else:
            value = card.value[0]  # some have a value of 'King' this changes that to a simple 'K' ("King" doesn't fit)
            space = ' '  # no "10", we use a blank space to will the void
        # get the cards suit in two steps
        suit = suits_name.index(card.suit)
        suit = suits_symbols[suit]

        # add the individual card on a line by line basis
        lines[0].append('┌─────────┐')
        lines[1].append('│{}{}       │'.format(value, space))  # use two {} one for char, one for space or char
        lines[2].append('│         │')
        lines[3].append('│    {}    │'.format(suit))
        lines[4].append('│         │')
        lines[5].append('│       {}{}│'.format(space, value))
        lines[6].append('└─────────┘')
        display_index += 1
        if printIndices == True:
            lines[7].append('   [{:>2}]    '.format(display_index))
        
        counter += 1
        if counter == 5:
            result = []
            for index, line in enumerate(lines):
                result.append(''.join(lines[index]))
            print('\n'.join(result))
            if printIndices == True:
                lines = [[] for i in range(8)]
            else:
                lines = [[] for i in range(7)]
            counter = 0
    result = []
    for index, line in enumerate(lines):
        result.append(''.join(lines[index]))
    if counter > 0:
        print('\n'.join(result))