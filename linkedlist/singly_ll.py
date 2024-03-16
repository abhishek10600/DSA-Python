class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, data):  # inserting an element at the head
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_at_end(self, data):  # insert an element at the end
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        curr_node = self.head
        while curr_node.next:
            curr_node = curr_node.next
        curr_node.next = new_node

    def insert_at_index(self, data, index):  # insert at index positing
        new_node = Node(data)
        position = 0
        if position == index:
            self.insert_at_head(data)
        else:
            curr_node = self.head
            while curr_node != None and position + 1 != index:
                position = position + 1
                curr_node = curr_node.next
            if curr_node != None:
                new_node.next = curr_node.next
                curr_node.next = new_node
            else:
                print("Index is not present")

    def update_node(self, val, index):  # update the data in a node at a given index
        curr_node = self.head
        position = 0
        if position == index:
            curr_node.data = val
        else:
            while curr_node != None and position != index:
                position = position + 1
                curr_node = curr_node.next
            if curr_node != None:
                curr_node.data = val
            else:
                print("Index is not present.")

    def delete_at_head(self):  # delete a node at head
        if self.head is None:
            return
        self.head = self.head.next

    def delete_at_end(self):  # delete a node at end
        if self.head is None:
            return
        curr_node = self.head
        while curr_node.next.next:
            curr_node = curr_node.next
        curr_node.next = None

    def print_list(self):  # print a linked list
        curr_node = self.head
        while (curr_node):
            print(curr_node.data)
            curr_node = curr_node.next


ll = LinkedList()
ll.insert_at_head(1)
ll.insert_at_head(2)
ll.insert_at_head(3)
ll.insert_at_end(5)
ll.insert_at_end(6)
ll.insert_at_index(7, 2)
ll.update_node(9, 2)
ll.delete_at_head()
ll.delete_at_end()
ll.print_list()
