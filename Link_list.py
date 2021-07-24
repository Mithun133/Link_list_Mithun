# # Linked list implementation in Python


# class Node:
#     # Creating a node
#     def __init__(self, item):
#         self.item = item
#         self.next = None


# class LinkedList:

#     def __init__(self):
#         self.head = None


# if __name__ == '__main__':

#     linked_list = LinkedList()

#     # Assign item values
#     linked_list.head = Node(1)
#     second = Node(2)
#     third = Node(3)
#     third = Node(20)

#     # Connect nodes
#     linked_list.head.next = second
#     second.next = third

#     # Print the linked list item
#     while linked_list.head != None:
#         print(linked_list.head.item, end=" ")
#         linked_list.head = linked_list.head.next






# # Single Linked List Implementation
                                        

# class Node:                                      
#     """ This class create a node"""
#     def __init__(self, data='Head', next=None):
#         self.data = data
#         self.next = next

# class LinkedList:
#     def __init__(self):
#         self.head = Node()

#     def insert_at_beginning(self, data):
#         # node = Node(2, 0xH40)
#         node = Node(data, self.head.next)
#         self.head.next = node

#     def print_linked_list(self):
#         if self.head.next is None:
#             print('Linked list is Empty.')
#             return
        
#         current_node = self.head
#         # Until current_node != None
#         res_str = ''
#         while current_node != None:
#             res_str = res_str + str(current_node.data) + ' --> '
#             current_node = current_node.next

#         print(res_str)

# if __name__ == '__main__':
#     # ll --> linked list
#     # node = head|None
#     ll = LinkedList()
#     ll.insert_at_beginning(15)
#     ll.insert_at_beginning(10)
#     ll.insert_at_beginning(5)
#     ll.insert_at_beginning(20)
#     ll.insert_at_beginning(30)
#     ll.print_linked_list()





# class Node:
#     def __init__(self, data='Head', next=None):
#         self.data = data
#         self.next = next

# class LinkedList:
#     def __init__(self):
#         self.head = Node()

#     def insert_at_beginning(self, data):
#         node = Node(data, self.head.next)
#         self.head.next = node

#     def print_linked_list(self):
#         if self.head.next is None:
#             print('Linked list is empty. ')
#             return

#         current_node = self.head
#         res_str = ''
#         while current_node != None:
#             res_str = res_str + str(current_node.data) + ' --> '
#             current_node = current_node.next

#         print(res_str)

# if __name__ == '__main__':
#     # ll --> linked list
#     # node = head|None
#     ll = LinkedList()
#     ll.insert_at_beginning(15)
#     ll.insert_at_beginning(10)
#     ll.insert_at_beginning(5)
#     ll.insert_at_beginning(20)
#     ll.insert_at_beginning(30)
#     ll.print_linked_list( )

   

# class Node:
#     def __init__(self, data='head',next=None):
#         self.data = data
#         self.next = next

# class LinkedList:
#     def __init__(self):
#         self.head = Node()

#     def insert_at_beginning(self, data):
#         node = Node(data, self.head.next)
#         self.head.next = node

#     def print_linked_list(self):
#         if self.head.next is None:
#             print('Link list is empty.')
#             return
#         current_node = self.head
#         res_str = ''
#         while current_node != None:
#             res_str = res_str + str(current_node.data) + ' ---> '
#             current_node = current_node.next

#         print(res_str)

# if __name__ == '__main__':
#     ll = LinkedList()
#     ll.insert_at_beginning(100)
#     ll.insert_at_beginning(200)
#     ll.insert_at_beginning(300)
#     ll.insert_at_beginning(400)
#     ll.print_linked_list()






class Node:
    def __init__(self, data= 'Head', next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = Node()

    def get_length(self):
        count = 0
        n = self.head
        while n:
            count = count + 1
            n = n.next
            return count

    def insert_at_beginning(self, data):
        node = Node(data, self.head.next)
        self.head.next = node

    def print_link_list(self):
        if self.head.next is None:
            print('Linked list is empty.')
            return

        current_node = self.head
        res_str = ''
        while current_node != None:
            res_str = res_str + str(current_node.data) + ' ----> '
            current_node = current_node.next

        print(res_str)

# ---------------------------------------------------------Searching--------------------------------------------

    def search(self,search_item):
        current_node = self.head.next

        while current_node !=None:
            if current_node.data == search_item:
                print('\n Data found in link list.')
                return
            current_node = current_node.next
        print('\n Opps! Data not found') 

    # -----------------------------------------------------remove-----------------------------------------------------
    def remove(self, remove_item):
        if self.head is None:
            print("Can't delete because LL is empty.")
            return
        pre = self.head
        current_node = pre.next

        while current_node != None:
            if current_node.data == remove_item:
                break
            pre = current_node
            current_node = pre.next
        pre.next = current_node.next

        # removing 1st item

        # if x == self.head.data:
        #     self.head = self.head.next
        #     return

        # n = self.head
        # while n.next is not None:
        #     if x == n.next.data:
        #         break
        #     n = n.next

        # if n.next is None:
        #     print("Node is not present")
        # else:
        #     n.next = n.next.next

# ------------------------------------------------------Insert-------------------------------------------------
    def insert_at(self, location, data):
        # if location<0 or location>self.get_length:
        #     print('Invalid location')
        #     return
        if location == 0:
            self.insert_at_beginning(data)
            return
        cnt = 0
        current_node = self.head
        while current_node != None:
            if cnt == location - 1:
                node = Node(data, current_node.next)
                current_node.next = node
                break
            current_node = current_node.next
            cnt += 1



if __name__ == '__main__':
    ll = LinkedList()
    print("\nAdded elements at begining : ")
    ll.insert_at_beginning(50)
    ll.insert_at_beginning(100)
    ll.insert_at_beginning(150)
    ll.insert_at_beginning(200)
    ll.insert_at_beginning(250)
    ll.insert_at_beginning(500)
    ll.print_link_list()


    ll.search(150)
    ll.search(100)
    ll.print_link_list()

    print("\nAfter removing element: ")
    ll.remove(50)
    ll.remove(500)
    ll.print_link_list()

    print("\n\nAfter inserting element: ")
    ll.insert_at(2, 25)
    ll.insert_at(4, 45)
    ll.print_link_list()

