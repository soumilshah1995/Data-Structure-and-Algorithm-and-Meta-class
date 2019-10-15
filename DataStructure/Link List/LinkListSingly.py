
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def set_data(self, new_data):
        self.data = new_data

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next

    def __repr__(self):
        return "Node Object > {}".format(self.data)


class LinkList(object):

    def __init__(self):
        self.head = None

    def addNode(self, Data):
        Tem = Node(Data)
        Tem.set_next(self.head)
        self.head = Tem

    def deleteNode(self, data):
        if self.head is None:
            return "Cannot Delete as Link list is empty"
        else:
            current = self.head
            previous = None
            found = False

            while not found:
                if current.get_data() == data:
                    found = True
                else:
                    if current.get_next() is None:
                        return "Element cannot be deleted as its not in Link List "
                    else:
                        previous = current
                        current = current.get_next()

            if previous is None:
                self.head = current.get_next()
            else:
                previous.set_next(current.get_next())

    def size(self):
        size = 0
        if self.head is None:
            return size
        else:
            current = self.head
            while current is not None:
                size = size + 1
                current = current.get_next()
            return size

    def isEmpty(self):
        return self.head is None

    def search(self, data):

        if self.head is None:
            return " Link List is Empty cannot Search Data"
        else:
            found = False
            current = self.head
            while current is not None :
                if current.get_data() == data:
                    return True
                else:
                    current = current.get_next()
            return False

def main():
    node = LinkList()
    node.addNode(1)
    node.addNode(2)
    node.addNode(3)
    node.addNode(4)
    print("Size : ", node.size())
    print("Empty : ", node.isEmpty())
    print("Deleting 3",node.deleteNode(3))
    print("Size : ", node.size())
    print("Empty : ", node.isEmpty())


if __name__ == "__main__":
    main()


