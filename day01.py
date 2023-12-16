### Definitions
import inflect

WORDS = {}
for i in range(1,10):
    WORDS[inflect.engine().number_to_words(i)] = str(i)

def get_first_dig(word, part = 1) -> str:
    for idx, char in enumerate(word):
            try:
                return str(int(char))
            except:
                if part == 2:
                    for i in range(idx):
                        substr = word[i:idx+1]
                        try:
                            return WORDS[substr]
                        except:
                            pass

def get_last_dig(word) -> str:
    for idx in range(len(word),-1,-1):
            try:
                return str(int(word[idx]))
            except:
                for i in range(idx+2,len(word)+1):
                    substr = word[idx:i]
                    try:
                        return WORDS[substr]
                    except:
                        pass

### Import
with open('inpt01') as f:
    lines = [line.strip() for line in f]

### Part 1
fin_sum = 0
for line in lines:
    numbers = get_first_dig(line)
    fin_sum += int(numbers + get_first_dig(line[::-1]))
print(fin_sum)

### Part 2
fin_sum = 0
for line in lines:
    numbers = get_first_dig(line, 2)
    fin_sum += int(numbers + get_last_dig(line))
print(fin_sum)
