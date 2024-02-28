
class Node:
    def __init__(self, data, priority) -> None:
        self.data = data
        self.priority = priority
        self.next = None
        self.prev = None

    def __str__(self):
        return self.data + " priority: " + str(self.priority)
    

class PriorityQueue:
    def __init__(self) -> None:
        self.head = None
        self.tail = None 

    def insert(self, data, priority):
        node = Node(data, priority)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            iter = self.head
            while iter is not None and iter.priority < priority:
                iter = iter.next
            if iter is None:  # it was the highest priority, we reached the end
                self.tail.next = node 
                node.prev = self.tail 
                self.tail = node
            else:
                if iter == self.head:
                    iter.prev = node 
                    node.next = iter 
                    self.head = node
                else: 
                    iter.prev.next = node 
                    node.prev = iter.prev 
                    iter.prev = node
                    node.next = iter





    def peek(self):
        # return the highest priority Node without removing
        pass

    def remove(self):
        # remove and return the highest priority Node
        if self.tail is None:
            return None
        elif self.tail == self.head:
            node = self.tail
            self.tail = None
            self.head = None
        else:
            node = self.tail 
            self.tail = self.tail.prev 
            self.tail.next = None
        return node


    def traverse(self):
        # visit and print each node, just for testing
        iter = self.head
        while iter is not None:
            print(iter)
            iter = iter.next

    def change_priority(self, data, new_priority):
        pass 


if __name__ == "__main__":
    pq = PriorityQueue()
    pq.insert("Peter", 0)
    pq.insert("Ann", 0)
    pq.insert("Tom", 1)
    pq.insert("James", 0)
    pq.insert("Nick", 4)
    pq.insert("Alice", 1)
    pq.insert("Jim", 3)
    pq.traverse()
    node = pq.remove()
    print("Serve: ", node)
    pq.traverse()



