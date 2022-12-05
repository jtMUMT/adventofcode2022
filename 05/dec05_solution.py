# Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?

from dec05_input_data import *
from dec05_config import *

import numpy as np
from distutils.command import install

#CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
#          WAREHOUSE STATE
#CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
class Warehouse():
    def __init__(self,init_state):
        self.init_state = np.asarray(init_state)
        [self.stacks, self.num_stacks] = self.initStack(self.init_state)
        self.stack_tops = np.zeros(self.num_stacks) # list of empty spots in each stack
        self.updateStackTops()
        
    def __str__(self):
        outstr = ""
        for row in self.stacks:
            for col in row:
                outstr = outstr + chr(int(col)) + " "
            outstr = outstr + "\n"
        return outstr
    
    #------------------------------------
    #   PRINT TOP BOXES
    #------------------------------------
    def topBoxes(self):
        outstr = ""
        num_cols = np.size(self.stack_tops)
        for col in range(num_cols):
            top_spot = int(self.stack_tops[col] - 1)
            top_box = self.stacks[top_spot, col]
            outstr = outstr + chr(int(top_box))
        return outstr
    
    #------------------------------------
    #   INIT THE STACKS
    #------------------------------------
    def initStack(self,init_state):
        # for each column, we're gonna reverse gravity
        # so index 0 will be the floor
        # and then we'll pad out the stacks. They'll be overly large
        # but today I can't be arsed to resize them dynamically
        
        # any stack will be capable of holding as many boxes as there are spots
        # in the initial grid (includes empty spots for now)
        num_cols = np.size(init_state,1)
        max_stack_size = np.size(init_state)
        stacks = np.zeros([max_stack_size,num_cols])
        
        # split into columns
        for col in range(num_cols):
            this_stack = init_state[:,col] # get the column
            this_stack = np.flip(this_stack) # reverse so index 0 is floor
            stacks[0:np.size(this_stack),col] = this_stack # overwrite this col into the stack
    
        return [stacks, num_cols]
            
            
    #------------------------------------
    #   UPDATE THE STACK POINTERS
    #------------------------------------
    def updateStackTops(self):
        # find the first zero in each stack
        for col in range(self.num_stacks):
            empty_spot = np.min(np.where(self.stacks[:,col] == 0))
            self.stack_tops[col] = int(empty_spot)
        return True
    
    #------------------------------------
    #   MOVE CRATES BETWEEN STACKS
    #------------------------------------
    def move(self,instruction):
        
        if VERBOSE:
            print("MOVE:\n",instruction)
            print("BEFORE:")
            print(self)
            
        num_crates = instruction[0]
        source_stack = instruction[1] - 1
        target_stack = instruction[2] - 1
        
        source_top = int(self.stack_tops[source_stack])
        target_top = int(self.stack_tops[target_stack])
        
        # copy the crates off the source stack
        crates_held = np.copy(self.stacks[source_top - num_crates:source_top, source_stack])
        # flip the contents (we place them back down in reverse order)
#         crates_held = np.flip(crates_held) # NO LONGER APPLIES IN PART 2
        # zero out the source stack spots
        self.stacks[source_top - num_crates:source_top, source_stack] = np.zeros(np.size(crates_held))
        # overwrite the top spots in the target stack
        self.stacks[target_top:target_top+num_crates,target_stack] = crates_held
        
        if VERBOSE:
            print("AFTER:")
            print(self)
        
        # finish by updating the stack top info
        self.updateStackTops()
        
        return
        

##########################################
#            PARSE INPUT FN
##########################################
# Sorts out the raw data into meaningful objects
#
def processRawData(raw_data):
    # split the initial state diagram from the instructions
    [raw_init_state, raw_instructions] = raw_data.split(INPUT_SECTIONS_DELIM)
    
    # parse the stack diagram, specifically
    init_state = parseStackDiagram(raw_init_state)
    
    # parse the instructions, specifically
    instructions = parseInstructions(raw_instructions)
    
    
    return [init_state, instructions]

##########################################
#            PARSE STACK DIAGRAM
##########################################
# Specifically parsing the input section that has the diagram of the stacks
#
def parseStackDiagram(raw_init_state):
    
    # first strip out all the square brackets
    raw_init_state = raw_init_state.replace(BOX_OPEN_BRACKET,"")
    raw_init_state = raw_init_state.replace(BOX_CLOSE_BRACKET,"")
    
    # split into rows
    raw_rows = raw_init_state.split(INPUT_STACK_ROWS_DELIM)
    
    # throw out the last row, we know it's not important
    raw_rows = raw_rows[0:-1]
    cooked_rows = []
    
    # now process the rest of the rows
    for row in raw_rows:
        # first split by 4 spaces so that "empty" columns become addressable columns
        # instead of lots of whitespace
        stripped_row = row.split(INPUT_STACK_EMPTY_COL_DELIM)
        
        cooked_row = []
        # rows that have adjacent "boxes" will need to be stripped by " " again
        for sr in stripped_row:
            col = sr.split(INPUT_STACK_COLUMNS_DELIM)
            for c in col:
                # while we're here let's switch everything to integer representation
                if c == "":
                    c = 0
                else:
                    c = ord(c)
                cooked_row.append(c)
        cooked_rows.append(cooked_row)
    return cooked_rows

##########################################
#            PARSE STACK DIAGRAM
##########################################
# Specifically parsing the input section that has the diagram of the stacks
#
def parseInstructions(raw_instructions):
    
    # first strip out all the words. They're always in the same semantic order
    # so we don't need them
    raw_instructions = raw_instructions.replace(INSTRUCTION_MOVE,"")
    raw_instructions = raw_instructions.replace(INSTRUCTION_SOURCE,"")
    raw_instructions = raw_instructions.replace(INSTRUCTION_TARGET,"")
    
    cooked_instructions = []
    
    # now we can simply split by line, then by whitespace.
    inst_rows = raw_instructions.split(INSTRUCTION_LINES_DELIM)
    for inst in inst_rows:
        inst = inst.split() #split by whitespace
        inst = [int(i) for i in inst] # convert to integer
        cooked_instructions.append(inst)
        
            

    return cooked_instructions  

##########################################
#            MAIN FUNCTION
##########################################
def main():
    
    if USE_TEST_INPUT:
        [init_state, instructions] = processRawData(test_input)
    else:
        [init_state, instructions] = processRawData(raw_input)
        
    warehouse = Warehouse(init_state)
    
    for inst in range(len(instructions)):
        warehouse.move(instructions[inst])
        
    print("FINAL CONFIGURATION:")
    print(warehouse)
    print(warehouse.topBoxes())

##########################################
#           SCRIPT EXECUTION
##########################################
if __name__ == "__main__":
    main()