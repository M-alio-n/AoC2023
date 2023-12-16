### Definitions
def find_numerals(string: str, res_list: list, offset: int = 0) -> None:
    found = False
    for idx1 in range(len(string)):
        idx2 = idx1+1
        while string[idx1:idx2].isdigit() and idx2 <= len(string)+1:
            idx2 += 1
            found = True
        if found:
            idx2 = idx2-1
            res_list.append((idx1+offset,idx2+offset))
            find_numerals(string[idx2::], res_list, idx2+offset)
            return

def check_neighbours(lines, line_idx: int, nums_idx: tuple):
    fields_to_check = list_neighbours(lines, line_idx, nums_idx)
    for tup in fields_to_check:
        if not lines[tup[0]][tup[1]] == '.':
            return int(lines[line_idx][nums_idx[0]:nums_idx[1]])
    return 0

def list_neighbours(lines, line_idx: int, nums_idx: tuple):
    res_list = []
    for line_ind in range(max([0, line_idx-1]), min([len(lines), line_idx+2])):
        if not line_ind == line_idx:
            for pos_ind in range(max([0, nums_idx[0]-1]), min([len(lines[line_idx]), nums_idx[1]+1])):
                res_list.append((line_ind, pos_ind))
        else:
            if nums_idx[0] > 0:
                res_list.append((line_ind, nums_idx[0]-1))
            if nums_idx[1] < len(lines[line_idx]):
                res_list.append((line_ind, nums_idx[1]))
    return res_list

def count_neighbours(numbers_pos, line_idx, fields_to_check, lines):
    nums = [set(),set(),set()]
    for field in fields_to_check:
        for number in numbers_pos[field[0]]:
            if field[1]>=number[0] and field[1]<number[1]:
                nums[field[0]-line_idx+1].add(number)
    if sum(len(nums[i]) for i in range(3)) == 2:
        vals = []
        for i in range(3):
            for tup in nums[i]:
                vals.append(int(lines[line_idx-1+i][tup[0]:tup[1]]))
        return vals[0]*vals[1]
    return 0
    
### Import
with open('inpt03') as f:
    lines = [line.strip() for line in f]

### Part 1
fin_sum = 0
numbers_pos = []
for line_idx, line in enumerate(lines):
    numbers_pos.append([])
    find_numerals(line, numbers_pos[-1])
    fin_sum += sum(check_neighbours(lines,line_idx,tup) for tup in numbers_pos[-1])
print(fin_sum)

### Part 2
fin_sum = 0
for line_idx, line in enumerate(lines):
    gears = [i for i, char in enumerate(line) if char == '*']
    for gear in gears:
        fields_to_check = list_neighbours(lines, line_idx, (gear,gear+1))
        fin_sum += count_neighbours(numbers_pos, line_idx, fields_to_check, lines)
print(fin_sum)