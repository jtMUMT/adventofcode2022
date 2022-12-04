# Set False for "production" obv
DEBUG_PRINT = False
VERBOSE = True

# More debugging (I'm so hungover lol)
PROBLEM_TRIALS = [1,56]
USE_TEST_INPUT = False

# Setting up the priority numbers for each letter
LOWERCASE_MIN = ord("a")
LOWERCASE_MAX = ord("z")
LOWERCASE_OFFSET = -ord("a") + 1

UPPERCASE_MIN = ord("A")
UPPERCASE_MAX = ord("Z")
UPPERCASE_OFFSET = -ord("A") + 27

# I'll be using the letter IDs as lookups in a data
# structure and then doing logical operations on that structure.