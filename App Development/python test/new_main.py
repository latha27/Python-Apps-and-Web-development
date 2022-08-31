class TrainComposition:

    def __init__(self):
        self.wagons = dict()
        self.left  = 1
        self.right = 0

    def attach_wagon_from_left(self, wagonId):
        self.left -= 1
        self.wagons[self.left] = wagonId


    def attach_wagon_from_right(self, wagonId):
        self.right += 1
        self.wagons[self.right] = wagonId


    def detach_wagon_from_left(self):
        if self.left>self.right: return None
        wagonId = self.wagons[self.left]
        del self.wagons[self.left]
        self.left += 1
        return wagonId


    def detach_wagon_from_right(self):

        if self.left>self.right: return None
        wagonId = self.wagons[self.right]
        del self.wagons[self.right]
        self.right -= 1
        return wagonId




if __name__ == "__main__":
    train = TrainComposition()
    train.attach_wagon_from_left(7)
    train.attach_wagon_from_left(13)
    print(train.detach_wagon_from_right())  # should print 7
    print(train.detach_wagon_from_left())  # should print 13