class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Linked:
    def __init__(self):
        self.head = None


    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, self.head)
            return
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)



    def print(self):
        if self.head is None:
            print("List is Empty")
            return

        itr  = self.head
        liststr  = ''

        while itr:
            liststr  += str(itr.data) + "-->"
            itr = itr.next
        return print(liststr)


if __name__=='__main__':
    ll = Linked()
    ll.insert_at_end(5)
    ll.insert_at_end(9)
    ll.insert_at_end(6)
    ll.insert_at_end(13)
    ll.insert_at_end(51)

    ll.print()

