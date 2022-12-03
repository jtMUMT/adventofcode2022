# Constants and whatnot for Dec02 coding puzzle

# R/P/S selection codes for oppponent and for "me"
# I'm arranging this as 2-element lists with the first being the opponent's
# choice of RPS code (A B or C) and the 2nd being the corresponding win, 
# draw or loss code for my selection (X Y or Z)

# For clarity:
# THEIR CODE      MY WIN      MY DRAW     MY LOSS
# A               Y           X           Z
# B               Z           Y           X
# C               X           Z           Y

# Index labels for grabbing the relevant codes from the lookup table
WIN = 0
DRAW = 1
LOSS = 2

# For part 2 we're throwing the match, and our codes
# now represent the following desired match result. All
# this really means is that we'll add an extra layer of 
# translation and then re-use our old code for the 
# processing of the round. I'm using these labels just to
# make this file a little bit more readable
MUST_LOSE = "X"
MUST_DRAW = "Y"
MUST_WIN = "Z"

# Here is the lookup table for part 2
THROW_LOOKUP = {
    "A": {MUST_WIN:"Y", MUST_DRAW:"X", MUST_LOSE:"Z"},
    "B": {MUST_WIN:"Z", MUST_DRAW:"Y", MUST_LOSE:"X"},
    "C": {MUST_WIN:"X", MUST_DRAW:"Z", MUST_LOSE:"Y"},
    }

# Here is the lookup table for part 1
RPS_LOOKUP = {
    "A": {"Y":WIN, "X":DRAW, "Z":LOSS},
    "B": {"Z":WIN, "Y":DRAW, "X":LOSS},
    "C": {"X":WIN, "Z":DRAW, "Y":LOSS},
    }

# And the corresponding scoring lookups
CHOICE_SCORE = {"X":1, "Y":2, "Z":3}
RESULT_SCORE = [6,3,0] #win/draw/lose
