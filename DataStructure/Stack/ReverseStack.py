
""""
FIFO
"""

class Stack(object):

    def __init__(self):
        self.item = []

    def push(self, item):

        """

        :param item: Accepts item as Parameter
        :return: None
        """
        self.item.append(item)


    def pop(self):
        """
        This will remove Last item
        :return: None
        """
        return self.item.pop()


    def peek(self):
        """
        Allows us to see the Last elements
        :return: Last item
        """
        if self.item:
            return self.item[-1]
        else:
            return None

    def size(self):
        if self.item:
            return len(self.item)
        else:
            return None

    def isempty(self):

        """
        tells Whether the stack is Empty or not
        :return: Bool Value
        """
        return self.item == []


def reverse(str):

    stack = Stack()
    mystr = ''

    for i in range(len(str)):
        stack.push(str[i])

    str = ''

    while not stack.isempty():
        Tem = stack.pop()
        str = str + Tem
    return str




if __name__ == "__main__":
    reverse("Soumil")










