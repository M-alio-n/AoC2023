### Definitions
card_order = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
type_order = ['hc', '1p', '2p', '3k', 'fh', '4k', '5k']

class CamelHand():
    def __init__(self, hand) -> None:
        self.bid = int(hand.split()[1])
        self.hand = hand.split()[0]
        self.type = det_type(self.hand)
        self._inds = all_inds(self.hand, 'J')

    def set_max_type(self):
        curr_idx = 0
        for tmp_hand in iter(self):
            if type_order.index(det_type(tmp_hand)) > curr_idx:
                self.type = det_type(tmp_hand)
                curr_idx = type_order.index(det_type(tmp_hand))
                if self.type == '5k':
                    break

    def __lt__(self, other):
        if type_order.index(self.type) < type_order.index(other.type):
            return True
        if type_order.index(self.type) > type_order.index(other.type):
            return False
        for idx, char in enumerate(self.hand):
            if card_order.index(char) < card_order.index(other.hand[idx]):
                return True
            if card_order.index(char) > card_order.index(other.hand[idx]):
                return False
        return None
    
    def __iter__(self):
        self._curr_inds = [0 for i in self._inds]
        if len(self._curr_inds) > 0:
            self._curr_inds[-1] = -1
        self._tmp_hand = self.hand
        return self
    
    def __next__(self):
        if len(self._curr_inds) == 0 or all(i==12 for i in self._curr_inds):
            raise StopIteration
        (self._tmp_hand, self._curr_inds) = increase_hand(
            self._tmp_hand, self._inds, self._curr_inds)
        return_hand = self._tmp_hand
        return return_hand

def increase_hand(hand, inds, curr_inds):
    new_curr_inds = increase_inds(curr_inds, len(curr_inds)-1)
    new_hand = hand
    for idx, char_idx in enumerate(inds):
        new_hand = new_hand[0:char_idx] + card_order[curr_inds[idx]] + new_hand[char_idx+1::]
    return (new_hand, new_curr_inds)

def increase_inds(inds, pos):
    inds[pos] += 1
    if inds[pos] == 13:
        inds[pos] = 0
        increase_inds(inds, pos-1)
    return inds

def det_type(hand: str):
    counts = [hand.count(char) for char in list(dict.fromkeys(list(hand)))]
    if len(counts) == 1:
        return '5k'
    if len(counts) == 2 and counts[0] in [4,1]:
        return '4k'
    if len(counts) == 2 and counts[0] in [2,3]:
        return 'fh'
    if len(counts) == 3 and 3 in counts:
        return '3k'
    if len(all_inds(counts, 2)) == 2:
        return '2p'
    if len(all_inds(counts, 2)) == 1:
        return '1p'
    return 'hc'

def all_inds(check_list, item):
    res_list = []
    for idx, val in enumerate(check_list):
        if val == item:
            res_list.append(idx)
    return res_list
### Import
with open('inpt07') as f:
    hands = [CamelHand(line.strip()) for line in f]

### Part 1
hands.sort()
print(sum(hand.bid*(rank+1) for rank,hand in enumerate(hands)))

### Part 2
card_order.insert(0, card_order.pop(9))
for hand in hands:
    hand.set_max_type()
hands.sort()
print(sum(hand.bid*(rank+1) for rank, hand in enumerate(hands)))