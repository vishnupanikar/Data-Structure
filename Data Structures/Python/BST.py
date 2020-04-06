#----------------------------------Node Type data-------------------------------------
class Node:
      def __init__(self):
            self.data = 0
            self.leftchild = None
            self.rightchild = None

#---------------------------------Inserting into BST--------------------------------------
def insert(root , data):
      if root == None:
            node = Node()
            node.data = data
            return node
      elif data > root.data:
            root.rightchild = insert(root.rightchild , data)
            return root
      else:
            root.leftchild = insert(root.leftchild , data)
            return root

#-----------------------------------Inorder traversal(Sorted Order)------------------------------------
def inorder(root):
      if root == None:
            return
      else:
            inorder(root.leftchild)
            print(root.data , end='-->')
            inorder(root.rightchild)
            return

#-----------------------------------Preorder traversal------------------------------------
def preorder(root):
      if root == None:
            return
      else:
            print(root.data , end='-->')
            preorder(root.leftchild)
            preorder(root.rightchild)
            return

#-------------------------------------Postoredr Traversal----------------------------------
def postorder(root):
      if root == None:
            return
      else:
            postorder(root.leftchild)
            postorder(root.rightchild)
            print(root.data , end='-->')
            return

#-----------------------------------Searching in BST------------------------------------
def search(root , element):
      if root == None:
            print('No Such Element')
            return
      elif root.data == element:
            print('Element Found')
            return
      elif element > root.data:
            search(root.rightchild , element)
            return
      else:
            search(root.leftchild , element)
            return

#--------------------------------MAIN---------------------------------------
if __name__ == '__main__':

      n = int(input('Enter the number of nodes :: '))
      root = None

      for i in range(n):
            data = int(input('Enter Node Value :: '))
            root = insert(root,data)
      
      print("Inorder :: " , end = '')
      inorder(root)
      print("\nPreorder :: " , end = '')
      preorder(root)
      print("\nPostorder :: " , end = '')
      postorder(root)


      element = int(input('\nEnter the element to be searched :: '))
      search(root , element)
