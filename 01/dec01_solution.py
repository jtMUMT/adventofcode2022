# Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?

from dec01_input_data import *
import numpy as np


#CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
#
#            ELF CLASS
#
#CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
class Elf():
    def __init__(self,inventory):
        self.inventory = np.asarray(inventory)
        
    def countCalories(self):
        total = np.sum(self.inventory)
        return total

##########################################
#            PARSE INPUT FN
##########################################
def chunkRawData(raw_data, delimiter):
    double_delimiter = delimiter + delimiter
    split_data_by_elf = raw_data.split(double_delimiter)
    elves = []
    for foodbag in split_data_by_elf:
        items_str = foodbag.split(delimiter)
        items_int = []
        for item in items_str:
            items_int.append(int(item))
        elves.append(Elf(items_int))
    return elves
        
##########################################
#     FIND MOST CALORIFIC ELF BAG
##########################################
def findMostCalorificElfBag(elves):
    most_calories = 0
    for elf in elves:
        this_calories = elf.countCalories()
        if this_calories > most_calories:
            most_calories = this_calories
    return most_calories

##########################################
#            MAIN FUNCTION
##########################################
def main():
    elves = chunkRawData(raw_input,"\n")
    most_cals = findMostCalorificElfBag(elves)
    print("MOST CALORIES CARRIED BY AN ELF:")
    print(most_cals)
        

##########################################
#           SCRIPT EXECUTION
##########################################
if __name__ == "__main__":
    main()