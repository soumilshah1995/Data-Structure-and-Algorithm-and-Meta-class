"""
DEQUE Abstract Data Type

DEQUE = Double ended Queue

High level its combination of stack and queue

you can insert item from  front and back
You can remove items from front and back

we can use a list  for this example. we will use methods

>----- addfront
>----- add rear
>----- remove front
>----- remove rear

we want to check Size, isempty
QUEUE - FIFO
STACK - LIFO

DEQUE - can use both LIFO or FIFO
any items you can store in list can be stored in DEQUE

Most common Questions is Palindrone
using DEQUE Datastructure

"""


class Deque(object):

    def __init__(self):
        self.items = []

    def add_front(self, item):
        self.items.insert(0, item)

    def add_rear(self, item):
        self.items.append(item)

    def remove_front(self):
        return self.items.pop(0)

    def remove_rear(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def isempty(self):

        if(self.items) == []:
            return True
        else:
            return False

    def peek_front(self):
        return self.items[0]

    def peek_rear(self):
        return self.items[-1]


def main(data):

    deque = Deque()
    for character in data:
        deque.add_rear(character)

    while deque.size() >= 2:
        front_item = deque.remove_front()
        rear_item = deque.remove_rear()

        if rear_item != front_item:
            return False
    return True


if __name__ == "__main__":
    print(main("nitin"))
    print(main("car"))