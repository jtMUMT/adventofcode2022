# Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?

from dec03_input_data import *
from dec03_config import *

import numpy as np

##########################################
#            PARSE INPUT FN
##########################################
# Converts the input data a list of 2 lists for later processing
#
def processRawData(raw_data, bag_delimiter):
    # split into bags
    raw_bags = raw_data.split(bag_delimiter)
    bags = []
    # convert all bag items to priority numbers
    for bag in raw_bags:
        pbag = [] # pbag as in priority-coded bag
        # convert to priority number
        for i in range(len(bag)):
            pbag.append(calcItemPriority(bag[i]))
        # then split the bag in two
        midpoint = int(len(pbag)/2)
        bag_split = [pbag[0:midpoint],pbag[midpoint:]]
        bags.append(bag_split) 
    return bags

##########################################
#           CALC ITEM PRIORITY
##########################################
# Determines the priority # of a character (a-z or A-Z)
#
def calcItemPriority(item):
    item_ord = ord(item)
    # if this is a lowercase letter apply the lowercase offset
    if (LOWERCASE_MIN <= item_ord <= LOWERCASE_MAX):
        priority = item_ord + LOWERCASE_OFFSET
    # if this is a uppercase letter apply the uppercase offset
    elif (UPPERCASE_MIN <= item_ord <= UPPERCASE_MAX):
        priority = item_ord + UPPERCASE_OFFSET
    else:
        print("invalid item letter detected")
        priority = -1
    return priority

##########################################
#            CALC BAG SCORES
##########################################
# Determines the score of each bag based on whichever item is shared between the 2 compartments
#
def calcBagScores(bags):
    
    # predefining the matrix dimensions (see below)
    num_rows = calcItemPriority("Z") + 1
    num_cols = 2
    
    # init the score
    score = 0
    
    # For each bag
    for bag in bags:
        # Create a data structure that will be used as a logical lookup
        # It has a number of rows equal to the number of priorities, and a column for each compartment
        checklist = np.zeros([num_rows,num_cols])
        # for each item in (both) compartments, flag the appropriate position in the data structure and calculate the output if found.
        score = score + checkForMatch(checklist,bag)
    return score

##########################################
#         CHECK ONE BAG FOR MATCH
##########################################
def checkForMatch(checklist, bag):
    score = 0 # init just in case
    # first iterating over each row
    for i in range(np.size(bag,1)):
        # then over each of the 2 comparments
        for j in range(np.size(bag,0)):
            item_priority = bag[j][i]
            # flag the presence of this item
            checklist[item_priority][j] = 1
            # look for a match on this row
            if np.sum(checklist[item_priority]) > 1:
                score = item_priority
                return score
    return score

##########################################
#            MAIN FUNCTION
##########################################
def main():
    bags = processRawData(raw_input,"\n")
    total = calcBagScores(bags)
    print("TOTAL SCORE:")
    print(total)

##########################################
#           SCRIPT EXECUTION
##########################################
if __name__ == "__main__":
    main()