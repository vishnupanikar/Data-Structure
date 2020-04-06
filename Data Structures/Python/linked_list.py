
# Python does not support pointers so we store the object location in another object 

#---------------Node for the linked list---------
class Node:
      def __init__(self):
            self.data = None
            self.next = None

#-------------Create linked list--------------
def create(head , data):
      node = Node()
      node.data = data

      if head == None:
            head = node
      else:
            temp = head            # this is correct as temp is a label pointing to the object same as head
                                   # change in temp means temp is now pointing to a new object and head is still pointing to the original object
                                   #so retaining the start of the linked list
            while(temp.next != None):
                  temp = temp.next
            temp.next = node
      return head

#------------Inserting new head---------------
def insert_head(head,data):
      node = Node()
      node.data = data
      node.next = head
      head = node
      return head

#-----------Inserting at index-------------
def insert_index(head , data , pos):
      i = 0
      while(i < (pos -2)):
            head = head.next
            i += 1

      node = Node()
      node.data = data
      node.next = head.next
      head.next = node
#------------Deleting head--------------
def delete_head(head):
      head = head.next
      return head

#-------------Deleting at index---------------
def delete_index(head , pos):
      i = 0
      while(i < (pos -2)):
            head = head.next
      head.next = head.next.next

#------------Displaying Linked list-------------
def display(head):
      print()
      while head != None:
            print(head.data , end = '-->')
            head = head.next
      print()
#--------------Main-------------------
if __name__ == '__main__':
      head_node = None
      #----------------Creating Linked List-------------------
      node_count = int(input("Enter Number of nodes :: "))
      for i in range(node_count):
            data = int(input("Enter node Value :: "))
            head_node = create(head_node , data)
      
      #----------------Displaying the list-----------------
      display(head_node)

      #--------------Inserting new head---------------
      data = int(input("Enter node Value :: "))
      head_node = insert_head(head_node , data)
      display(head_node)

      #------------inserting at index------------
      data = int(input("Enter node Value :: "))
      pos = int(input('Enter Position :: '))
      insert_index(head_node,data,pos)
      display(head_node)

      #------------deleting head--------------
      head_node = delete_head(head_node)
      display(head_node)

      #------------deleting at index-----------
      pos = int(input('Enter Position :: '))
      delete_index(head_node , pos)
      display(head_node)
