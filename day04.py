### Definitions
class ScratchCard():
    def __init__(self, string) -> None:
        self._winning_nums = [i for i in string.split(':')[1].split('|')[0].split(' ') if i]
        self._chosen_nums = [i for i in string.split(':')[1].split('|')[1].split(' ') if i]
        self._wins = sum(1 for i in self._chosen_nums if i in self._winning_nums)
        self._amount = 1
    
    def get_wins(self):
        return self._wins
    
    def get_amount(self):
        return self._amount
    
    def get_worth(self):
        return int(2**(self._wins-1))

    def create_copies(self, amount):
        self._amount += amount
    
    def __radd__(self, other):
        if isinstance(other, ScratchCard):
            return self._amount + other._amount
        if isinstance(other, (int, float)):
            return self._amount + other

### Import
with open('inpt04') as f:
    cards = [ScratchCard(line.strip()) for line in f]

### Part 1
fin_sum = 0
for card in cards:
    fin_sum += card.get_worth()
print(fin_sum)

### Part 2
for card_idx, card in enumerate(cards):
    for i in range(card.get_wins()):
        cards[card_idx+1+i].create_copies(card.get_amount())
print(sum(cards))
