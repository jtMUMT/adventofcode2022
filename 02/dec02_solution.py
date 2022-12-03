# Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?

from dec02_input_data import *
from dec02_config import *

import numpy as np

##########################################
#            PARSE INPUT FN
##########################################
# Converts the input data a list of 2-element lists for later processing
#
def chunkRawData(raw_data, round_delimiter, choice_delimiter):
    raw_rounds = raw_data.split(round_delimiter)
    cooked_rounds = []
    for r in raw_rounds:
        this_round = r.split(choice_delimiter)
        cooked_rounds.append(this_round)
    return cooked_rounds
        
##########################################
#     SCORE A ROUND
##########################################
#
# Given a 2-element list of choices, calculate the score
#
def calcRoundScore(their_choice, my_choice):
    result = RPS_LOOKUP[their_choice][my_choice]
    score = RESULT_SCORE[result] + CHOICE_SCORE[my_choice]
    return score

##########################################
#     CHOOSE BASED ON DESIRED RESULT
##########################################
#
# Given a 2-element list of choices, calculate the score
#
def forceDesiredResult(their_choice, my_desired_result):
    new_choice = THROW_LOOKUP[their_choice][my_desired_result]
    return new_choice


##########################################
#            MAIN FUNCTION
##########################################
def main():
    rounds = chunkRawData(raw_input,"\n"," ")
    total = 0
    for r in rounds:
        their_choice = r[0]
        my_desired_result = r[1]
        my_choice = forceDesiredResult(their_choice, my_desired_result)
        total = total + calcRoundScore(their_choice, my_choice)
        
    print("TOTAL SCORE:")
    print(total)
    
        

##########################################
#           SCRIPT EXECUTION
##########################################
if __name__ == "__main__":
    main()