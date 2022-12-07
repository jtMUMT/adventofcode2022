from dec07_input_data import *
from dec07_config import *

import numpy as np

#CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
#            DIRECTORY CLASS
#CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
class Directory():
    def __init__(self,name, parent, root_dir):
        self.name = name
        self.parent = parent
        self.root = root_dir
        self.children = {}
        self.files = {}
        self.size = 0
        
        if self.parent:
            self.depth = self.parent.depth + 1
        else:
            self.depth = 0
        
    def __str__(self):
        this_indent = INDENT * self.depth
        to_print = this_indent + "|_  " + DIR_MARKER + " " + self.name + INDENT + "(dir: " + str(self.size) + ")\n"
        for c in self.children:
            to_print = to_print + str(self.children[c])
        for name,size in self.files.items():
            to_print = to_print + this_indent + INDENT + "|_  " + name + INDENT + "(file: " +  str(size) +  ")\n"
        return to_print
    
    #------------------------------------
    #   ADD SUBDIRECTORY
    #------------------------------------
    def addChild(self,subdir):
        child_name = subdir.name
        self.children[child_name] = subdir
        # self.calcSize()
        
    #------------------------------------
    #   ADD FILE
    #------------------------------------
    def addFile(self,name,size):
        self.files[name] = size
        # self.calcSize()
    
    #------------------------------------
    #   CALCULATE DIR SIZES
    #------------------------------------
    def calcSize(self):
        self.size = 0
        
        if len(self.children) != 0:
            for c in self.children:
                self.size = self.size + self.children[c].calcSize()
        if len(self.files) != 0:
            for name,size in self.files.items():
                self.size = self.size + size
                
        return self.size
    
    #------------------------------------
    #   GET ALL DIRS UNDER A CERTAIN SIZE
    #------------------------------------
    def getDirsBySizeLimit(self,dir_list, min_size, max_size):
        self.calcSize() # in case it hasn't been done before
        
        # if this dir is under the limit, add it to the provided list
        if min_size <= self.size <= max_size:
            dir_list.append(self)
        
        # now pass this call down our child dirs
        if len(self.children) != 0:
            for c in self.children:
                dir_list = self.children[c].getDirsBySizeLimit(dir_list,min_size,max_size)
                           
        return dir_list
    
    #------------------------------------
    #   CHANGE DIR
    #------------------------------------
    def changeDir(self,dirName):
        if dirName == BACK:
            return self.parent
        elif dirName == ROOT:
            if self.name == ROOT:
                return self
            else:
                return self.root
        else:
            return self.children[dirName]
        return -1 # shouldn't get here
                
        
        
##########################################
#            PARSE INPUT FN
##########################################
# Sorts out the raw data into meaningful objects
#
# In today's case, into lines that we will process later
#
def processRawData(raw_data):
    # split the messages by line break
    rows = raw_data.splitlines()
    for r in range(len(rows)):
        rows[r] = rows[r].split() # split by whitespace
    return rows

##########################################
#            RUN CLI COMMANDS
#            AND BUILD FILE SYSTEM
##########################################
# Run or interpret the command line printout
# and in doing so, construct the directory/file structure
#
def buildDirStruct(rows):
    # Firstly, we know that the root directory is a directory
    dir_struct = Directory(ROOT, None, None)
    root_dir = dir_struct
    current_dir = dir_struct
    
    # Run through the rows in order
    for r in rows:
        # Every line will start with either a command or a dir/file
        if r[0] == PROMPT:
            if r[1] == CHG_DIR:
                new_dir = r[2]
                current_dir = current_dir.changeDir(new_dir)
            # for ls command, there is nothing for us to do.
            elif r[1] == LIST_DIR:
                x = "DONT CARE"
        # If it's not a cd command, it's a dir or file within the current dir
        elif r[0] == DIR_MARKER:
            current_dir.addChild(Directory(r[1],current_dir,root_dir))
        else: # it's a file with a size
            size = int(r[0])
            name = r[1]
            current_dir.addFile(name,size)
    return dir_struct

##########################################
#            MAIN FUNCTION
##########################################
def main():
    
    if USE_TEST_INPUT:
        data = processRawData(test_input)
    else:
        data = processRawData(raw_input)
        
    dir_struct = buildDirStruct(data)
    
    dir_struct.calcSize()
    print(dir_struct)
    
    print("TOTAL DISK SPACE:",TOTAL_DISKSPACE)    
    print("USED:",dir_struct.size)
    print("MAX DISK USAGE:",MAX_DISK_USAGE)
    
    space_remaining = TOTAL_DISKSPACE - dir_struct.size
    print("DISK SPACE REMAINING:",space_remaining)
    
    space_needed = dir_struct.size - MAX_DISK_USAGE
    print("NEED TO FREE UP:",space_needed)
    
    print("")
    search_low = space_needed
    search_high = TOTAL_DISKSPACE
    
    print("TOTAL BETWEEN:",search_low,"and",search_high,":")
    dirs_under_limit = dir_struct.getDirsBySizeLimit([], search_low, search_high)
    
    total_under_limit = 0
    
    # this is so hacky. SORRY
    sizes = []
    
    for d in dirs_under_limit:
        print(d.name,d.size)
        total_under_limit = total_under_limit + d.size
        sizes.append(d.size)
    print("Total",total_under_limit)
    
    sizes.sort()
    print("Smallest of these has a size of",sizes[0])
    
    
    
    

##########################################
#           SCRIPT EXECUTION
##########################################
if __name__ == "__main__":
    main()