from singly_linked_list import SinglyLinkedList
from faker import Faker

class HashTable:
    size = 10

    def __init__(self) -> None:
        self.hash_table = [None] * self.size

    def get_hash_value(self, s: str) -> int:
        total = 0
        for c in s:
            total += ord(c)
        return total % self.size
    
    def insert(self, s: str) -> None:
        hash_value = self.get_hash_value(s)
        if self.hash_table[hash_value] is None:
            self.hash_table[hash_value] = SinglyLinkedList()
        self.hash_table[hash_value].insert_front(s)

    def display(self):
        for i in range(self.size):
            if self.hash_table[i] is None:
                print("None")
            else:
                self.hash_table[i].display()

    def search(self, s: str) -> bool:
        pass

    def remove(self, s: str) -> str:
        pass

    def restructure(self, size: int) -> None:
        pass



if __name__ == "__main__":
    print("HASH TABLE EXAMPLE")
    faker = Faker()
    ht = HashTable()
    for i in range(40):
        ht.insert(faker.first_name())
    ht.display()