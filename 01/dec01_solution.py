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
#     SORT ELF BAGS
##########################################
def sortElvesByCalories(elves):
    elf_sorted_amount = []
    for e in range(len(elves)):
        elf_sorted_amount.append(elves[e].countCalories())
    elf_sorted_amount.sort()
    elf_sorted_amount.reverse()
    return elf_sorted_amount

##########################################
#            MAIN FUNCTION
##########################################
def main():
    elves = chunkRawData(raw_input,"\n")
    most_cals = findMostCalorificElfBag(elves)
    print("MOST CALORIES CARRIED BY AN ELF:")
    print(most_cals)
    
    #determining sum of top 3 elf bags
    sorted_elf_bags = np.asarray(sortElvesByCalories(elves))
    top_3_sum = np.sum(sorted_elf_bags[0:3])
    print("SUM OF TOP 3 ELF BAGS:")
    print(top_3_sum)       
        

##########################################
#           SCRIPT EXECUTION
##########################################
if __name__ == "__main__":
    main()