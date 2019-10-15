import numpy as np
import datetime


start = datetime.datetime.now()

class Sort(object):

    def __init__(self):
        pass

    @staticmethod
    def merge(left_list, right_list):

        sorted_list = []
        left_list_index = right_list_index = 0
        left_list_length = len(left_list)
        right_list_length = len(right_list)

        for _ in range(left_list_length + right_list_length):

            if left_list_index < left_list_length and right_list_index < right_list_length:

                if left_list[left_list_index] < right_list[right_list_index]:
                    sorted_list.append(left_list[left_list_index])
                    left_list_index = left_list_index + 1
                else:
                    sorted_list.append(right_list[right_list_index])
                    right_list_index = right_list_index + 1

            elif left_list_index == left_list_length:
                sorted_list.append(right_list[right_list_index])
                right_list_index = right_list_index + 1

            elif right_list_index == right_list_length:
                sorted_list.append(left_list[left_list_index])
                left_list_index = left_list_index + 1

        return sorted_list

    def merge_sort(self, arr):

        if len(arr) <= 1:
            return arr
        else:
            mid = len(arr) // 2

            left_list = self.merge_sort(arr[:mid])
            right_list = self.merge_sort(arr[mid:])

            return Sort.merge(left_list, right_list)


def linear_search(data, target):
    data = Sort().merge_sort(data)
    for i in range(len(data)):
        if data[i] == target:
            return i
    return False


if __name__ == "__main__":
    np.random.seed(101)

    arr = np.random.randint(low=0, high=10000, size=[100000, 1])
    print(linear_search(arr, 121212))
    end = datetime.datetime.now()
    print("Total Time: {}".format(end - start))


