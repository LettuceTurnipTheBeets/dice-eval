#dice-eval.py
import random
import re

def parse(string):
    if len(string) > 0:
        dice_list = []
        string = string.replace(' ', '')
        average = 0

        """
        Loop while there are still dice to be rolled
        """
        while 'd' in string:
            pos1 = string.index('d') - 1
            pos2 = string.index('d') + 1

            while pos1 >= 0 and string[pos1] is not '+' and string[pos1] is not '-': 
                pos1 -= 1

            while pos2 < len(string) and string[pos2] is not '+' and string[pos2] is not '-': 
                pos2 += 1

            dice_list.append(string[pos1+1:pos2])
            string = string[0:pos1+1] + string[pos2:len(string)]

        number_list = [int(s) for s in re.findall("[-]?\d+", string)]
        total = sum(number_list)           
        average = total
        minimum = total
        maximum = total

        """
        Roll the dice and calculate the pseudorandomly rolled total, calculated average, calculated
        minimum, and calculated maximum
        """
        for dice in dice_list:
            index = dice.index('d')
            factor = int(dice[0:index])
            size = int(dice[index+1:len(dice)])

            total = total + (factor * roll_dice(size))
            average = average + (factor * (size + 1) / 2)
            minimum = minimum + factor
            maximum = maximum + (factor * size)

        print('Total: {}\nMinimum: {}\nAverage: {}\nMaximum: {}'.format(total, minimum, average, maximum))

def roll_dice(num):
    """
    Return one pseudorandom roll of a num-sided die
    """
    return random.randint(1, num)
