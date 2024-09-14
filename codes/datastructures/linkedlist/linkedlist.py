# Node Implementation


class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node):
        self.next_node = next_node

# Linked List Implementation


class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node

    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    def stringify_list(self):
        string_list = ""
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_value() != None:
                string_list += str(current_node.get_value()) + "\n"
            current_node = current_node.get_next_node()
        return string_list

    def remove_node(self, value_to_remove):
        current_node = self.get_head_node()
        if current_node and current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()
        else:
            while current_node:
                next_node = current_node.get_next_node()
                if next_node.get_value() == value_to_remove:
                    current_node.set_next_node(next_node.get_next_node())
                    current_node = None
                else:
                    current_node = next_node

    def remove_nodes_by_value(self, value_to_remove):
        while self.get_head_node() and self.get_head_node().get_value() == value_to_remove:
            self.head_node = self.get_head_node().get_next_node()
        current_node = self.get_head_node()
        while current_node:
            next_node = current_node.get_next_node()
            if next_node and next_node.get_value() == value_to_remove:
                current_node.set_next_node(next_node.get_next_node())
            else:
                current_node = next_node

# Testing The Code


New_List = LinkedList(0)
for i in range(1, 11):
    New_List.insert_beginning(i)
print(New_List.stringify_list())
New_List.remove_node(0)
print("removed head")
print(New_List.stringify_list())
for i in range(3):
    New_List.insert_beginning(1)
print("added 1's")
print(New_List.stringify_list())
New_List.remove_nodes_by_value(1)
print("removed 1's")
print(New_List.stringify_list())
