class Card(object):
    number = 0
    suit = None
    available = True
    
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit
    
    def __str__(self):
        return "{} {}".format(self.number, self.suit)
    
    def __repr__(self):
        return self.__str__()
    
    def is_available(self):
        return self.available
    
    def mark_available(self):
        self.available = True

    def mark_not_available(self):
        self.available = False


class Deck(object):
    cards = []
    deckColor = None
    dealtIndex = 0
    cardsType = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']

    def __init__(self, deck_color):
        self.cards = []
        self.deckColor = deck_color
        self._generate_cards()
        
    def _generate_cards(self):
        for i in self.cardsType:
            self.cards.append(Card(i, 'Club'))
            self.cards.append(Card(i, 'Diamond'))
            self.cards.append(Card(i, 'Heart'))
            self.cards.append(Card(i, 'Spade'))
        self.shuffle()
            
    def remaining_cards(self):
        return len(self.cards) - self.dealtIndex

    def shuffle(self):
        from random import shuffle
        shuffle(self.cards)


class Hand(object):
    cards = []
    
    def add_card(self, card):
        self.cards.append(card)

    @property
    def score(self):
        scores = [card.number for card in self.cards]
        return sum(scores)


class BriscolaDeck(Deck):
    cardsType = [1, 2, 3, 4, 5, 6, 7, 'J', 'Q', 'K']


if __name__ == '__main__':
    deck = Deck('RED')
    print "Deck: \n", deck.cards
    
    player1_hand = Hand()
    for x in range(10):
        player1_hand.add_card(deck.cards[x])
    print "Player1 Cards: \n", player1_hand.cards
    
    briscola = BriscolaDeck('BLACK')
    print briscola.cards
    print len(briscola.cards)
