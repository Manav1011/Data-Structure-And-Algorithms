class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        obj = Node(data, self.head)
        self.head = obj

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def print(self):
        if self.head is None:
            print("Link List is empty")
            return

        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data)+'---> '
            itr = itr.next

        llstr = llstr+'None'
        print(llstr)

    def get_length(self):
        self.length = 1
        count = 0
        itr = self.head
        if itr is None:
            print("Linked list is empty")
            return
        while itr.next:
            itr = itr.next
            count += 1
            self.length += 1
        return self.length

    def insert_values(self, values):
        for i in values:
            self.insert_at_end(i)

    def insert_at(self, index, data):
        list_length = self.get_length()
        if index > list_length + 1:
            print("List index out of bound")
            return
        itr = self.head

        if index == 1:
            self.head = Node(data, self.head)
            return
        itr = self.head
        for i in range(1, index - 1):
            itr = itr.next

        itr.next = Node(data, itr.next)

        itr.next = Node(data, itr.next.next)

    def delete_at(self, index):
        list_length = self.get_length()
        if index not in range(1, list_length):
            print("List index out of bound")
            return

        itr = self.head
        if index == 1:
            self.head = itr.next
            itr = None
            return
        for i in range(1, index - 1):
            itr = itr.next

        itr.next = itr.next.next

    def insert_after_value(self, value_after, value_to_insert):
        itr = self.head
        try:
            while itr.data != value_after:
                itr = itr.next

            itr.next = Node(value_to_insert, itr.next)
        except:
            print("Value out of bounds")

    def insert_before_value(self, value_before, value_to_insert):
        itr = self.head
        node_before_itr = None
        try:
            while itr.data != value_before:
                if itr.next.data == value_before:
                    node_before_itr = itr
                itr = itr.next

            node_before_itr.next = Node(value_to_insert, itr)
        except Exception as e:
            print(e)
            print("Value out of bounds")

    def remove_by_value(self, value):
        itr = self.head        
        try:
            while itr.data != value:
                if itr.next.data == value:
                    node_before_itr=itr
                itr = itr.next            
            itr.data = itr.next.data
            itr.next=itr.next.next
                        
        except Exception as e:
            print(e)


ll = LinkedList()
ll.insert_at_end(30)
ll.insert_at_beginning(5)
ll.insert_at_beginning(10)
ll.insert_at_beginning(20)
ll.get_length()
ll.insert_values([10, 20, 30, 40])
ll.insert_at(5,100)
ll.delete_at(4)
ll.insert_before_value(30,200)
ll.remove_by_value(20)
ll.print()
