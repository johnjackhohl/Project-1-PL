from collections import deque
import queue


def main():
    # start = input("Please enter a 4 digit dice roll:")
    startDiceRolls = "1234"
    startDice = [int(x) for x in str(startDiceRolls)]
    
    # end = input("Please enter what the previous dice roll should turn too: ")
    endDiceRolls = "4232"
    
    endDice = [int(x) for x in str(endDiceRolls)]
 
    path = bfs(startDice, endDice)
    print(shortestPath(path, startDice, endDice))
        
def bump(dice, pos):
    if dice[pos] >= 1 and dice[pos] <= 5:
        dice[pos]+=1
    return dice

def flip(dice, pos):
    dice[pos] = 7 - dice[pos]
    return dice

def swap(dice, pos1, pos2):
    temp = dice[pos1]
    dice[pos1] = dice[pos2]
    dice[pos2] = temp
    return dice

""" def graph(start, end):
    queue = [start]
    visited = []
    while queue:
        dice = queue.pop(0)
        if dice == end:
            return queue
        if dice not in visited:
            visited.append(dice)
            for i in range(4):
                queue.append(bump(dice[:], i))
                queue.append(flip(dice[:], i))
                for j in range(4):
                    if i != j:
                        queue.append(swap(dice[:], i, j))
    return None """

def bfs(start, end):
    path = {}
    visited = []
    queue = [(start, start)]
    while queue:
        current, prev = queue.pop(0)
        if current not in visited:
            visited.append(current)
            path[tuple(current)] = prev
            if current == end:
                return path
            for i in range(4):
                queue.append((bump(current[:], i), current))
                queue.append((flip(current[:], i), current))
                for j in range(4):
                    if i != j:
                        queue.append((swap(current[:], i, j), current))

def shortestPath(path, start, end):
   shortPath = []
   current = end
   while current != start:
    shortPath.append(current)
    current = path[tuple(current)]
   shortPath.append(start)
   shortPath.reverse()
   return shortPath

if __name__ == "__main__":
    main()