class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linked_list:
    def __init__(self):
        self.head = None

    def print_list(self):
        start = self.head
        while start is not None:
            print(start.data)
            start = start.next

    def insert_at_begin(self, new_value):
        start = self.head
        if start is None:
            new_node = Node(new_value)
            self.head = new_node
            new_node.next = None

        else:
            new_node = Node(new_value)
            self.head = new_node
            new_node.next = start

    def insert_at_end(self, new_value):
        start = self.head
        new_node = Node(new_value)
        while start.next is not None:
            start = start.next
        start.next = new_node


    # Deleting node which match with the value
    def del_node(self,value):
        start = self.head
        prev = start

        if self.head.data == value:
            self.head = self.head.next

        else:
            while start.data != value and start is not None:
                prev = start
                start = start.next

            if start is not None:
                prev.next = start.next

    def delete_at_position(self,pos):
        start = self.head
        prev = None
        p = 1

        if pos == 1:
            self.head = self.head.next

        else:
            while start is not None and p < pos:
                prev = start
                start = start.next
                p = p+1
            if start is not None:
                prev.next = start.next

    def len_using_recursion(self, node):
        start = node
        if start == None:
            return 0
        else:
            return 1 + self.len_using_recursion(start.next)


    def recursive_search(self,value,node):
        start = node
        if start is None:
            return False

        if start.data == value:
            return True

        return self.recursive_search(value,node.next)




if __name__ == '__main__':

    list1 = linked_list()
    node_1 = Node(1)
    node_2 = Node(4)
    node_3 = Node(5)

    list1.head = node_1
    node_1.next = node_2
    node_2.next = node_3


    list1.insert_at_begin(6)
    list1.insert_at_begin(8)
    list1.insert_at_end(10)
    list1.del_node(6)
    list1.delete_at_position(3)
    print("Total no.of elements in list is : {}".format(list1.len_using_recursion(list1.head)))
    print("During Recursive search we found ot that no is present : {}".format(list1.recursive_search(100, list1.head)))
    list1.print_list()

    # Inserting Node in a link list


