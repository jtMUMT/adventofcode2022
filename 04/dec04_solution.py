# Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?

from dec04_input_data import *
from dec04_config import *

import numpy as np

#CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
#
#            WORK ORDER CLASS
#
#CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
class WorkOrder():
    def __init__(self,start,finish):
        self.start = int(start)
        self.finish = int(finish)
        
    def isContainedWithin(self,their_workorder):
        if (their_workorder.start <= self.start) and (their_workorder.finish >= self.finish):
            return True
        else:
            return False
        
    def hasOverlap(self,their_workorder):
        # first eliminate full overlap possibility
        if self.isContainedWithin(their_workorder):
            return True
        # basically we're checking whether either of their endpoints straddle either of ours
        elif (their_workorder.start <= self.start and their_workorder.finish >= self.start) or (their_workorder.start <= self.finish and their_workorder.finish >= self.finish):
            return True
        else:
            return False
        
#CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
#
#            WORKGROUP CLASS
#
#CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
class WorkGroup():
    def __init__(self,members):
        self.members = members
    
#CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
#
#            ELF CLASS
#
#CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
class Elf():
    def __init__(self,work_order):
        self.work = work_order


##########################################
#            PARSE INPUT FN
##########################################
# Sorts out the raw data into meaningful objects
#
def processRawData(raw_data):
    # split by work group
    raw_groups = raw_data.split(GROUP_DELIM)
    # now process each workgroup
    work_groups = []
    for group in raw_groups:
        # split into work schedules
        schedules = group.split(SCHEDULE_DELIM)
        # assign each schedule to a worker
        workers = []
        for schedule in schedules:
            sections = schedule.split(SECTION_DELIM)
            order = WorkOrder(sections[0],sections[1])
            workers.append(Elf(order))
        work_groups.append(WorkGroup(workers))
    return work_groups

##########################################
#            CHECK FULL OVERLAPS
##########################################
# Reports the # of full overlaps in the given work groups
#
def checkFullOverlaps(work_groups):
    total_overlaps = 0
    non_overlaps = 0
    group_num = -1
    
    # This part is hard coded to only work with 2 workers. SORRY DAD
    # THIS IS TOTALLY GOING TO BITE ME IN PART 2 ISNT IT
    for group in work_groups:
        group_num += 1
        order0 = group.members[0].work
        order1 = group.members[1].work
        
        # DEBUGGING:\/\/\/\/\/
        for problem in PROBLEM_TRIALS:
            if group_num == problem:
                dummy = "put a breakpoint here"
        # DEBUGGING:/\/\/\/\/\
        
        if order0.isContainedWithin(order1) or order1.isContainedWithin(order0):        
            if VERBOSE: print("===OVERLAP===\nGroup",group_num,"\n",order0.start,"-",order0.finish,"\n",order1.start,"-",order1.finish)
            total_overlaps += 1
        else:
            non_overlaps += 1
    
    return [total_overlaps, non_overlaps]

##########################################
#            CHECK PART OVERLAPS
##########################################
# Reports the # of full overlaps in the given work groups
#
def checkPartOverlaps(work_groups):
    total_overlaps = 0
    non_overlaps = 0
    group_num = -1
    
    # This part is hard coded to only work with 2 workers. SORRY DAD
    # THIS IS TOTALLY GOING TO BITE ME IN PART 2 ISNT IT
    for group in work_groups:
        group_num += 1
        order0 = group.members[0].work
        order1 = group.members[1].work
        
        # DEBUGGING:\/\/\/\/\/
        for problem in PROBLEM_TRIALS:
            if group_num == problem:
                dummy = "put a breakpoint here"
        # DEBUGGING:/\/\/\/\/\
        
        if order0.hasOverlap(order1) or order1.hasOverlap(order0):        
            if VERBOSE: print("===OVERLAP===\nGroup",group_num,"\n",order0.start,"-",order0.finish,"\n",order1.start,"-",order1.finish)
            total_overlaps += 1
        else:
            non_overlaps += 1
    
    return [total_overlaps, non_overlaps]

##########################################
#            MAIN FUNCTION
##########################################
def main():
    
    if USE_TEST_INPUT:
        work_groups = processRawData(test_input)
    else:
        work_groups = processRawData(raw_input)
        
#     [full_overlaps, non_overlaps] = checkFullOverlaps(work_groups)
    
    [part_overlaps, non_overlaps] = checkPartOverlaps(work_groups)
    
#     print("FULL OVERLAPS: ", full_overlaps)
    print("PART OVERLAPS: ", part_overlaps)
#     print("NOT FULL OVERLAPS: ", non_overlaps)

##########################################
#           SCRIPT EXECUTION
##########################################
if __name__ == "__main__":
    main()