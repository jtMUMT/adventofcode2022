from dec06_input_data import *
from dec06_config import *

import numpy as np
        
##########################################
#            PARSE INPUT FN
##########################################
# Sorts out the raw data into meaningful objects
#
def processRawData(raw_data):
    # split the messages by line break
    rows = raw_data.splitlines()
    for r in range(len(rows)):
        rows[r] = list(rows[r])
    return rows

##########################################
#            START PACKET FIND
##########################################
# Sorts out the raw data into meaningful objects
#
def findStartPacket(messages):
    # starting from the 4th position,
    # move a sliding window over the input list
    # and in each window, determine whether the condition is met.
    # there are probably some very fun and clever optimizations here
    # but i'll just use a straightforward comparison
    # AKCHUALLY we can just use a string contain conditional
    # ACTUALLY NO THAT IS WRONG JUST DO THE MOST STRAIGHTFORWARD THING OK JEEZ
    positions = []
    for m in range(len(messages)):
        msg = messages[m]
        if VERBOSE: print(msg) #~~~~~~~~~~~~~~~~~VERBOSE
        positions.append(None)
        for pos in range(WINDOW_SIZE,len(msg)):
            window = msg[pos-WINDOW_SIZE:pos]
            if VERBOSE: print(pos,":",window) #~~~~~~~~~~~~~~~~~VERBOSE
            if len(np.unique(window)) == 4:
                positions[m] = pos
                break
    return positions

##########################################
#            MAIN FUNCTION
##########################################
def main():
    
    if USE_TEST_INPUT:
        messages = processRawData(test_input)
    else:
        messages = processRawData(raw_input)
        
    positions = findStartPacket(messages)
    
    print("PACKET START POSITIONS:")
    print(positions)

##########################################
#           SCRIPT EXECUTION
##########################################
if __name__ == "__main__":
    main()