### Definitions
class DestSourceMap():
    def __init__(self, map_list: list, ID: int):
        self._ID = ID
        self._ranges = []
        self._offsets = []
        self._title = map_list[0].split(' ')[0]
        for line in map_list[1::]:
            nums = list(map(int, line.split(' ')))
            self._ranges.append((nums[1],
                                  nums[1]+nums[2]))
            self._offsets.append(nums[0]-nums[1])
    
    def get_destination(self, source, maps):
        dest = source
        for idx, rang in enumerate(self._ranges):
            if rang[0] <= source < rang[1]:
                dest = source+self._offsets[idx]
                break
        if self._ID < len(maps)-1:
            return maps[self._ID+1].get_destination(dest, maps)
        return dest
    
    def get_destination_2(self, source, maps, same_step = 1e100):
        dest = source
        found_flag = False
        for idx, rang in enumerate(self._ranges):
            if rang[0] <= source < rang[1]:
                dest = source+self._offsets[idx]
                if rang[1] - source < same_step: 
                    same_step = rang[1] - source
                found_flag = True
                break
        if not found_flag:
            near_step = 1e100
            for idx, rang in enumerate(self._ranges):
                if source < rang[0] < near_step:
                    near_step = rang[0] - source
            if near_step < same_step:
                same_step = near_step
        if self._ID < len(maps)-1:
            return maps[self._ID+1].get_destination_2(dest, maps, same_step)
        return (dest, same_step)
    
### Import
with open('inpt05') as f:
    lines = [line.strip() for line in f]

target_seeds = list(map(int,lines.pop(0).split(' ')[1::]))

maps = []
curr_map = []
for line in lines[1::]:
    if line == '':
        maps.append(DestSourceMap(curr_map, len(maps)))
        curr_map = []
        continue
    curr_map.append(line)
maps.append(DestSourceMap(curr_map, len(maps)))

### Part 1
min_loc = 1e100
for seed in target_seeds:
    tmp = maps[0].get_destination(seed, maps)
    if tmp < min_loc:
        min_loc = tmp
print(min_loc)

### Part 2
min_loc = 1e100
for idx in range(0, len(target_seeds), 2):
    seed = target_seeds[idx]
    while seed < target_seeds[idx]+target_seeds[idx+1]:
        tmp = maps[0].get_destination_2(seed, maps)
        if tmp[0] < min_loc:
            min_loc = tmp[0]
        seed += tmp[1]
print(min_loc)
