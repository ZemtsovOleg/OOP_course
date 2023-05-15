class Card:
    def __init__(self, rank, suit) -> None:
        self.rank = rank
        self.suit = suit

    def __str__(self) -> str:
        return f'{self.rank} {self.suit}'


class Deck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

    def __init__(self) -> None:
        self.cards = [Card(rank, suit)
                      for suit in self.suits for rank in self.ranks]

    def __iter__(self):
        return iter(self.cards)


deck = Deck()
for card in deck:
    print(card)
