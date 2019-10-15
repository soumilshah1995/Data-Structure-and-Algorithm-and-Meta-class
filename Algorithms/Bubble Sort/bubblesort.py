import numpy as np
import datetime


start = datetime.datetime.now()

class Sort(object):

    def __init__(self, data):
        self.data = data

    @property
    def sort(self):
        for i in range(0, len(self.data)-1):
            for j in range(0, len(self.data)-1-i):
                if self.data[j] > self.data[j+1]:
                    Tem = self.data[j]
                    self.data[j] = self.data[j+1]
                    self.data[j+1] = Tem
        return self.data


def main():
    np.random.seed(101)
    arr = np.random.randint(low=0, high=100000, size=(1000000, 1))
    obj = Sort(arr)
    obj.sort
    end = datetime.datetime.now()
    print("Total Time: {}".format(end - start))


if __name__ == "__main__":
    main()