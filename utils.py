from enum import Enum

class player(Enum):
    PLAYER_X = 1
    PLAYER_O = 4

class boardState(Enum):
    PENDING = 0
    DRAW = 1
    WIN = 2