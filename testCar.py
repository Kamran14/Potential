from Vehicle import Car, Direction
import pytest

class Test:
    
    car = Car()

    def test_isMoving(self):
        self.car.direction = Direction.FORWARD
        assert self.car.isMoving(), "Car state: " + str(self.car.direction)

    def test_isNotMoving(self):
        self.car.direction = Direction.STOPPED
        assert not self.car.isMoving(), "Car state: " + str(self.car.direction)

    def test_moveForward(self):
        self.car.moveForward()
        assert self.car.direction == Direction.FORWARD, "Car state: " + str(self.car.direction)

    def test_moveBackward(self):
        self.car.moveBackward()
        assert self.car.direction == Direction.REVERSE, "Car state: " + str(self.car.direction)

    def test_stop(self):
        self.car.stop()
        assert self.car.direction == Direction.STOPPED, "Car state: " + str(self.car.direction)


    
