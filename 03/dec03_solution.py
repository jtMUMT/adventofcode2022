# Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?

from dec03_input_data import *
from dec03_config import *

import numpy as np

##########################################
#            PARSE INPUT FN
##########################################
# Converts the input data a list of 3 lists for later processing
#
def processRawData(raw_data, bag_delimiter):
    # split into bags
    raw_bags = raw_data.split(bag_delimiter)
    bags = []
    # convert all bag items to priority numbers
    for b in range(len(raw_bags)):
        bag = raw_bags[b]
        pbag = [] # pbag as in priority-coded bag
        # convert to priority number
        for i in range(len(bag)):
            pbag.append(calcItemPriority(bag[i]))
        # we don't bother splitting them into 2 compartments anymore
        # just add this to the bag collection
        if DEBUG_PRINT: print("raw:", bag,"\npri:", pbag, "\n") #~~~~~~~~~~~~~~~~~DEBUG
        bags.append(pbag)
    # now group the bags into groups of 3
    num_groups = int(len(bags)/3)
    groups = []
    for g in range(num_groups):
        idx = g*3 # start index for the next 3-elf chunk
        this_group = bags[idx:idx+3]
        groups.append(this_group)
        if DEBUG_PRINT: 
            print("===GROUP", g, "===\n", this_group,"\n") #~~~~~~~~~~~~~~~~~DEBUG
    return groups

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
        score = score + checkBagForMatch(checklist,bag)
    return score

##########################################
#            CALC GROUP SCORES
##########################################
# Determines the score of each bag based on whichever item is shared between the 2 compartments
#
def calcGroupScores(groups):
    
    # predefining the matrix dimensions (see below)
    num_rows = calcItemPriority("Z") + 1
    num_cols = 3
    
    # init the score
    score = 0
    group_number = -1 # for debugging mostly
    
    # For each group
    for group in groups:
        group_number += 1
        if VERBOSE: print("=======================\n", "Group # ", group_number) #~~~~~~~~~~~~~~~~~DEBUG
        for sus in PROBLEM_TRIALS: 
            if group_number == sus:
                dummy = "set a breakpoint here"
        # Create a data structure that will be used as a logical lookup
        # It has a number of rows equal to the number of priorities, and a column for each compartment
        checklist = np.zeros([num_rows,num_cols])
        # for each item in (both) compartments, flag the appropriate position in the data structure and calculate the output if found.
        score = score + checkGroupForMatch(checklist,group)
    return score

##########################################
#         CHECK ONE BAG FOR MATCH
##########################################
def checkBagForMatch(checklist, bag):
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
#         CHECK ONE GROUP FOR MATCH
##########################################
def checkGroupForMatch(checklist, group):
    score = 0 # init just in case
    # first iterating over each group member
    for i in range(len(group)):
#         if DEBUG_PRINT: print("group len:", len(group)) #~~~~~~~~~~~~~~~~~DEBUG
#         if DEBUG_PRINT: print("member\t",i) #~~~~~~~~~~~~~~~~~DEBUG
        # assuming each member has the same # of posessions
        for j in range(len(group[i])):
#             if DEBUG_PRINT: print("bag len:", len(group[0])) #~~~~~~~~~~~~~~~~~DEBUG
#             if DEBUG_PRINT: print("item\t",j) #~~~~~~~~~~~~~~~~~DEBUG
            item_priority = group[i][j]
            # flag the presence of this item
            checklist[item_priority][i] = 1
            # look for a match on this row.
            # if all three have this in their possession, we're good to go
            if np.sum(checklist[item_priority]) >= 3:
                if VERBOSE: print("COMMON ITEM:\t",item_priority) #~~~~~~~~~~~~~~~~~DEBUG
                score = item_priority
                return score
    return score

##########################################
#            MAIN FUNCTION
##########################################
def main():
    if USE_TEST_INPUT:
        groups = processRawData(test_input,"\n")
    else:
        groups = processRawData(raw_input,"\n")
    total = calcGroupScores(groups)
    print("TOTAL SCORE:")
    print(total)

##########################################
#           SCRIPT EXECUTION
##########################################
if __name__ == "__main__":
    main()