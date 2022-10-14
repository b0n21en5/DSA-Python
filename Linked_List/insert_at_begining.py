class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Linked:
    def __init__(self):
        self.head = None


    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node


    def print(self):
        if self.head is None:
            print("List is Empty")
            return

        itr  = self.head
        liststr  = ''

        while itr:
            liststr  += str(itr.data)
            itr = itr.next
        return print(liststr)
    

if __name__=='__main__':
    ll = Linked()
    for _ in range(5):
        ll.insert_at_begining(int(input()))

    ll.print()
