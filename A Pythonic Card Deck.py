import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = "spades diamonds clubs hearts".split()

    def __init___(self):
        self._cards = [Card(rank, suits) for suit in self.suits
                                         for rank in self.ranks]
                                        
    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

deck = FrenchDeck()


beer_card = Card('7', 'diamond')
print(beer_card)