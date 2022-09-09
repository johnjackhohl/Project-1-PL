def main():
    # starting dice roll
    start = input("Please enter a 4 digit dice roll:")
    # starting dice roll into array 
    dice = [int(x) for x in str(start)]
    # end dice roll
    end = input("Please enter what the previous dice roll should turn too: ")
    # end dice roll into array
    endDice = [int(x) for x in str(end)]
# adds one to one dice
def bump(dice, poss):
    if dice[poss] != 6:
        dice[poss]+=1
    return dice
# flips once dice to the opposite side
def flip(dice, poss):
    dice[poss] = 7 - dice[poss]
    return dice
# swaps two dice's possition
def swap(dice, poss1, poss2):
    temp = dice[poss1]
    dice[poss1] = dice[poss2]
    dice[poss2] = temp
    return dice

main()