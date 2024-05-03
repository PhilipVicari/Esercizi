from collections import Counter
def blackjack(cards: list[int])-> int:
    cards_num: int = sum(cards)
    num_aces: int = cards.count(1) + cards.count(11)

    while cards_num > 21 and num_aces > 0:
        cards_num==10
        num_aces==1
    return cards_num
print(blackjack([]))
def construct_rettangle(area: float)-> list[float]:
    combos= []
    for width in range(3, area +1):                         #Fase 1; Individuare le possibili combinazioni
        for height in range(1, area +1):
            if width + height == area and width >= height:
                combos.append([width, height])
    min_diff: float = float ('inf')  
    index_diff: int = 0                                     #Fase 2; individuare la differenza minima tra i due valori delle combinazioni
    for combo in combos:
        curr_diff: float = combo[0] - combo[1]
        if curr_diff <= min_diff:
            min_diff = curr_diff
            index_diff= 1
    return combos[index_diff]
#print(construct_rettangle(4))

def find_lhs(notes: list[int]) -> int:
    num_freg = dict(Counter(notes))

    max_length = 0
    for num in num_freg:
        if num +1 in num_freg:
            somma = num_freg[num] + num_freg[num +1]
        if somma>= max_length:
            max_length = somma 
    return max_length

def third_max(gems: list[int]) -> int:
    gems = sorted(list[set(gems)], reverse= True)
    if len(gems)>=3:
        return gems[2]
    else:
        return[0]
#print(third_max[(3, 2, 1)])
#print(third_max[(1, 2)])
#print(third_max[(2, 2, 3, 1)])

def binary_search(array: list[int], x: int)-> int:
    low = 0
    high = len(array)
    while low <= high:
        mid = (low + high)//2
        if array[mid] == x:
            return mid
        else:
            if x > array(mid):
                low = mid + 1
            else:
                high = mid - 1
    return None




def Media_per_livelli(tree: dict[int, list[int]], root: int):
    media={}
    stack: list[int] = [root, 0]
    while stack:
        curr_mode, curr_level = stack.pop(0)
        left_child, righ_child = tree.get(curr_mode, [None, None])
        if left_child:





tree = {4: [3,5], 3: [2, None], 5: [4.5, 6], 2: [None, None], 4.5: [None, None], 6: [None, None]}
# >>> 0:4, 1:4, 2: 4,16666666
print(Media_per_livelli(tree, ))