# Creating a Max Heap

class MaxHeap:
    def __init__(self) -> None:
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        pos = len(self.heap) - 1
        self.heapify_up(pos)

    def remove(self):
        if len(self.heap) == 0:
            return None
        value = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop(-1)
        self.heapify_down(0)
        return value

    def heapify_up(self, pos):
        while pos > 0:
            parent = self.get_parent_pos(pos)
            if self.heap[parent] < self.heap[pos]:
                self.heap[parent], self.heap[pos] = \
                    self.heap[pos], self.heap[parent]
                pos = parent
            else:
                break

    def heapify_down(self, pos):
        while pos is not None:
            max_child = self.get_max_child_pos(pos)
            if max_child is not None:
                if self.heap[max_child] > self.heap[pos]:
                    self.heap[max_child], self.heap[pos] = \
                        self.heap[pos], self.heap[max_child]
                else:
                    break
            pos = max_child
            
    def get_parent_pos(self, pos):
        return (pos - 1) // 2
    
    def get_max_child_pos(self, pos):
        left_pos = 2 * pos + 1
        right_pos = 2 * pos + 2
        if left_pos >= len(self.heap):
            return None 
        elif right_pos >= len(self.heap):
            return left_pos
        else:
            return left_pos if \
                self.heap[left_pos] > self.heap[right_pos] \
                else right_pos
    

if __name__ == "__main__":
    heap = MaxHeap()
    heap.insert(2)
    heap.insert(12)
    heap.insert(13)
    heap.insert(11)
    heap.insert(4)
    heap.insert(56)
    heap.insert(24)
    print(heap.heap)
    heap.remove()
    heap.remove()
    print(heap.heap)
