### Definitions
class CubeGame():
    def __init__(self, string: str) -> None:
        self._id = int(string.split(':')[0].split(' ')[1])
        self._sets = string.split(':')[1].split(';')

        for idx, set in enumerate(self._sets):
            # order: [red, green, blue]
            order = {'red': 0, 'green': 1, 'blue': 2}
            self._sets[idx] = [0,0,0]
            for comb in set.split(','):
                self._sets[idx][order[comb.split(' ')[2]]] = int(comb.split(' ')[1])

    def is_posible(self, test_set = (12, 13, 14)) -> int:
        for comb in self._sets:
            for i in range(3):
                if comb[i]>test_set[i]:
                    return 0
        return self._id
    
    def min_power(self):
        powers = [0,0,0]
        for comb in self._sets:
            for i in range(3):
                if comb[i]>powers[i]:
                    powers[i] = comb[i]
        return powers[0]*powers[1]*powers[2]

### Import
with open('inpt02') as f:
    games = [CubeGame(line.strip()) for line in f]

### Part 1
print(sum(game.is_posible() for game in games))
### Part 2
print(sum(game.min_power() for game in games))
