class ListNode:

    def __init__(self, key):
        self.key = key
        self.next = None


class MyHashSet:

    def __init__(self):
        # Max size for the number of insertions the problem has
        self.set = [ListNode(0) for i in range(10**4)]

    def add(self, key: int) -> None:
        index = key % len(self.set)  # Hash Function
        current_node = self.set[index]  # Head of the List

        while current_node.next:
            if current_node.next.key == key:  # Detecting a Duplicate
                return None
            current_node = current_node.next  # Travels to the end of the List
        current_node.next = ListNode(key)

    def remove(self, key: int) -> None:
        index = key % len(self.set)  # Hash Function
        current_node = self.set[index]

        while current_node.next:
            if current_node.next.key == key:
                current_node.next = current_node.next.next
                return None
            current_node = current_node.next

    def contains(self, key: int) -> bool:
        index = key % len(self.set)  # Hash Function
        current_node = self.set[index]

        while current_node.next:
            if current_node.next.key == key:  # Searches the Index for the value
                return True  # We found the value, then it returns True!
            current_node = current_node.next
        return False  # The List does not have the key we looked for, then it returns False
