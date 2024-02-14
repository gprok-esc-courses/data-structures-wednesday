
class Node:
    def __init__(self, value) -> None:
        self.element = value
        self.next = None

    def __str__(self):
        return self.element
    
    def set_next(self, ref):
        self.next = ref

    def get_next(self):
        return self.next
    
    def get_element(self):
        return self.element


class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None 

    def is_empty(self):
        return self.head is None and self.tail is None
    
    def insert_front(self, value):
        # create a new node
        new_node = Node(value)
        # set node's next to head
        new_node.set_next(self.head)
        # set head to the new node
        self.head = new_node
        # if tail is None point to the head
        if self.tail is None:
            self.tail = self.head

    def remove_first(self):
        if not self.is_empty():
            value = self.head.get_element()
            self.head = self.head.get_next()
            return value
        else:
            return None
        
    def remove(self, value):
        if not self.is_empty():
            # Check if value is the first element
            if self.head.get_element() == value:
                return self.remove_first()
            else:
                iterator = self.head
                while iterator is not None and \
                    iterator.get_next().get_element() != value:
                    iterator = iterator.get_next()
                if iterator is not None:
                    iterator.set_next(iterator.get_next().get_next())
                    return value
                else:
                    return None
        else:
            return None
        
    def insert_back(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.tail = new_node
            self.head = new_node 
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    def remove_back(self):
        if not self.is_empty():
            if self.head == self.tail:
                value = self.tail.get_element()
                self.head = None 
                self.tail = None
                return value
            else:
                iterator = self.head
                while iterator.get_next() != self.tail:
                    iterator = iterator.get_next()
                value = self.tail.get_element()
                self.tail = iterator
                self.tail.set_next(None)
                return value
        else:
            return None


    def display(self):
        if self.is_empty():
            print("List is empty")
        else:
            # set an iterator pointing where head points to
            iterator = self.head 
            # loop as long as iterator is not None and print iterator
            while iterator is not None:
                print(iterator)
                iterator = iterator.get_next()


class Stack(SinglyLinkedList):
    def __init__(self) -> None:
        super().__init__()

    def push(self, value):
        self.insert_front(value)

    def pop(self):
        return self.remove_first()


data = SinglyLinkedList()
data.insert_front("Athens")
data.insert_front("Paris")
data.insert_front("Tirana")
data.insert_front("Prague")
data.insert_front("London")
#data.remove_first()
#data.remove_back()
data.insert_back("Vienna")
data.remove("London")
data.display()