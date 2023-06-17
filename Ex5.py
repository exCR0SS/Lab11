class ArrayList:
    def __init__(self, N):
        self.arr = [*range(1, N + 1)]

    def removeEverySecondElement(self):
        i = 0
        while len(self.arr) != 1:
            if i == len(self.arr):
                i = 0
            self.arr.pop(i)
            i += 1

    def getLastElement(self):
        return self.arr[0]