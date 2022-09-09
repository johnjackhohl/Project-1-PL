def main():
    start = startPrompt()
    dice = [int(x) for x in str(start)]
    end = endPrompt()
# get the starting dice
def startPrompt():
    num = input("Please enter a 4 digit dice roll.")
    #add if statement to check that it is valid
    return int(num)
# get the ending dice
def endPrompt():
    num = input("Please enter what the previous dice roll should turn too.")
    return int(num)
# adds one to one dice
def bump(dice, poss):
    dice[poss] = dice[poss]+1
    return dice
# flips once dice to the opposite side
def flip(dice, poss):
    dice[poss] = 7 - dice[poss]
# swaps two dice's possition
def swap(dice, poss1, poss2):
    temp = dice[poss1]
    dice[poss1] = dice[poss2]
    dice[poss2] = temp
    return dice