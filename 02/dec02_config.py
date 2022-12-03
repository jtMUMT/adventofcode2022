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

# Here is the lookup table then
RPS_LOOKUP = {
    "A": {"Y":WIN, "X":DRAW, "Z":LOSS},
    "B": {"Z":WIN, "Y":DRAW, "X":LOSS},
    "C": {"X":WIN, "Z":DRAW, "Y":LOSS},
    }

# And the corresponding scoring lookups
CHOICE_SCORE = {"X":1, "Y":2, "Z":3}
RESULT_SCORE = [6,3,0] #win/draw/lose
