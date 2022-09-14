def main():
    startDiceRolls = input("Please enter a 4 digit dice roll: ")
    startDice = [int(x) for x in str(startDiceRolls)]

    endDiceRolls = input("Please enter the target dice roll: ")
    endDice = [int(x) for x in str(endDiceRolls)]

    path = bfs(startDice, endDice)
    print(shortestPath(path, startDice, endDice))


def bump(dice, pos):
    """Increases the value of the dice at the given position by 1"""
    if dice[pos] >= 1 and dice[pos] <= 5:
        dice[pos] += 1
    return dice


def flip(dice, pos):
    """Flips the value of the dice at the given position"""
    dice[pos] = 7 - dice[pos]
    return dice


def swap(dice, pos1, pos2):
    """Swaps the values of the dice at the given positions"""
    temp = dice[pos1]
    dice[pos1] = dice[pos2]
    dice[pos2] = temp
    return dice


def bfs(start, end):
    """Breadth First Search for the dice ladder

    Args:
        start (array): starting dice configuration
        end (array): ending dice configuration

    Returns:
        array: paths from start to end
    """
    queue = [start]
    path = {tuple(start): None}
    while queue:
        current = queue.pop(0)
        if current == end:
            return path
        for i in range(4):
            for j in range(4):
                if i != j:
                    new = swap(current[:], i, j)
                    if tuple(new) not in path:
                        queue.append(new)
                        path[tuple(new)] = current
        for i in range(4):
            new = bump(current[:], i)
            if tuple(new) not in path:
                queue.append(new)
                path[tuple(new)] = current
        for i in range(4):
            new = flip(current[:], i)
            if tuple(new) not in path:
                queue.append(new)
                path[tuple(new)] = current
    return path


def shortestPath(path, start, end):
    """Finds the shortest path from start to end

    Args:
        path (array): path from start to end
        start (array): starting dice configuration
        end (array): ending dice configuration

    Returns:
        array: shortest path from start to end
    """
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
