from dec08_input_data import *
from dec08_config import *

import numpy as np

##########################################
#            PARSE INPUT FN
##########################################
# Sorts out the raw data into meaningful objects
#
# In today's case, into lines that we will process later
#
def processRawData(raw_data):
    # split the messages by line break
    raw_rows = raw_data.splitlines()
    cooked_rows = []
    for row in raw_rows:
        cooked_rows.append(list(row))
    cooked_rows = np.asarray(cooked_rows)
    return cooked_rows

##########################################
#            IS TREE VISIBLE
##########################################
def isTreeVisible(trees,x,y):
    # first off, if the tree is on an edge
    # it's automatically visible
    if x == 0 or x == np.size(trees,0)-1 or y == 0 or y == np.size(trees,1)-1:
        return 1
    
    # for each of 4 cardinal directions,
    # check if this tree's height # is
    # higher than every other tree up to the
    # edge of the grid
    my_height = trees[x,y]
    
    sightlines = []
    visible_paths = 4
    
    if x == 2 and y == 3:
        dummy = "break here"
    
    # NORTH
    sightlines.append(trees[x,y-1::-1])
    # SOUTH
    sightlines.append(trees[x,y+1:])
    # EAST
    sightlines.append(trees[x+1:,y])
    # WEST
    sightlines.append(trees[x-1::-1,y])
    
    for line in sightlines:
        for tree in line:
            if tree >= my_height:
                visible_paths = visible_paths - 1
                break
    
    if visible_paths > 0:
        return 1
    else:
        return 0
    
##########################################
#            SCORE SCENERY
##########################################
def scenicScore(trees,x,y):
    # any edge will have a score of zero
    if x == 0 or x == np.size(trees,0)-1 or y == 0 or y == np.size(trees,1)-1:
        return 0
    
    # for each of 4 cardinal directions,
    # determine how far until a tree
    # is equal or higher than this tree
    my_height = trees[x,y]
    
    sightlines = []
    sight_scores = []
    
    if x == 1 and y == 2:
        dummy = "break"
    
    # NORTH
    sightlines.append(trees[x,y-1::-1])
    # SOUTH
    sightlines.append(trees[x,y+1:])
    # EAST
    sightlines.append(trees[x+1:,y])
    # WEST
    sightlines.append(trees[x-1::-1,y])
    
    for line in sightlines:
        sight_score = 0
        for tree in line:
            if tree < my_height:
                sight_score = sight_score + 1
            else:
                sight_score = sight_score + 1
                break
            
        sight_scores.append(sight_score)
            
    final_score = np.prod(sight_scores)
    
    return final_score
                

##########################################
#            MAIN FUNCTION
##########################################
def main():
    
    if USE_TEST_INPUT:
        data = processRawData(test_input)
    else:
        data = processRawData(raw_input)
        
    print(np.size(data,0),":",np.size(data,1))
                
    scores = []
    
    for row in range(np.size(data,0)):
        for column in range(np.size(data,1)):
            score = scenicScore(data, row, column)    
            scores.append(score)        
            print(row,column,":",score)
            
    print("Highest scenery score:", np.max(scores))
    
##########################################
#           SCRIPT EXECUTION
##########################################
if __name__ == "__main__":
    main()