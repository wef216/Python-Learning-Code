import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                         for rank in self.ranks]
                                        
    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

deck = FrenchDeck()
print(len(deck))
print(deck[1])

### Randomly choose a card
from random import choice
print(choice(deck))
print(choice(deck))


### deck is iterable
for card in deck[1:14]:
    print(card)


### in method
print(Card("A","spades") in deck)
print(Card("As","spades") in deck) 

