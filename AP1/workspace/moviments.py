'''
MOVIMENTS
--------------------------------------------------------------------------------
Below we have all the possibilities of movement on the board

FROM     = Position where the piece is on the board
MOVEMENT = All the moves you can do with the piece
TO       = Positions where the piece will be on the board after the chosen move


FROM            0                 1                     2
MOVEMENT    down right      left down right         left down
TO            3    1          0    4    2             1    5


FROM             3                 4                    5
MOVEMENT    up down right   left up down right     left up down
TO           0   6   4       3   1   7    5         4   2   8


FROM            6                  7                     8
MOVEMENT    up right         left up right           left up
TO           3   7             6   4   8               7   5              

left  = position - 1
up    = position - 3
down  = position + 3
right = position + 1
================================================================================
'''

def to_left(from_position):
    return from_position - 1

def to_up(from_position):
    return from_position - 3

def to_down(from_position):
    return from_position + 3

def to_right(from_position):
    return from_position + 1

MOVIMENTS = {
    0: ["down", "right"],
    1: ["left", "down", "right"],
    2: ["left", "down"],
    3: ["up", "down", "right"],
    4: ["left", "up", "down", "right"],
    5: ["left", "up", "down"],
    6: ["up", "right"],
    7: ["left", "up", "right"],
    8: ["left", "up"],
}

NEXT_POSITION = {
    "left": to_left,
    "up": to_up,
    "down": to_down,
    "right": to_right,
}

def calcule_next_position(choice, current_position):
    position_calculator = NEXT_POSITION[choice]
    return position_calculator(current_position)