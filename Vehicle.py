import enum, pytest

class Direction(enum.Enum):
    FORWARD = 1
    REVERSE = 2
    STOPPED = 3


class Car:
    direction = Direction.STOPPED
    
    def __init__(self):
        self.direction = Direction.STOPPED

    def isMoving(self):
        return bool(self.direction != Direction.STOPPED)
    
    def moveForward(self):
        self.direction = Direction.FORWARD

    def moveBackward(self):
        self.direction = Direction.REVERSE

    def stop(self):
        self.direction = Direction.STOPPED
