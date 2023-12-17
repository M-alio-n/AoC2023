import numpy as np

### Definitions
def beat_it(time, record):
    distances = np.array(range(time+1))*(time-np.array(range(time+1)))
    return sum(distances > record)

def beat_it_2(time, record):
    h0 = np.floor(time/2 - np.sqrt((time**2)/4 - record))
    h1 = np.floor(time/2 + np.sqrt((time**2)/4 - record))
    return h1-h0

### Import
with open('inpt06') as f:
    lines = [line.strip() for line in f]
times = list(map(int, lines[0].split()[1::]))
records = list(map(int, lines[1].split()[1::]))

### Part 1
ways_to_win = []
for time, record in zip(times, records):
    ways_to_win.append(beat_it(time, record))
print(np.prod(ways_to_win))

### Part 2
print(beat_it_2(int(''.join(map(str, times))), int(''.join(map(str, records)))))
