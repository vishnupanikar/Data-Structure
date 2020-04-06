#Defining maximum size for the stack
max_size = 10

#--------------------Stack ADT---------------
class Stack:
    
      #------------------------intializations------------
      #---------both are private
      def __init__(self):
            self.__top = -1
            self.__stack = [0]*max_size

      #----------------------isFull---------------------
      def isFull(self):
            if self.__top == max_size-1:
                  return True
            else:
                  return False
      
      #----------------------isEmpty---------------------
      def isEmpty(self):
            if self.__top == -1:
                  return True
            else:
                  return False

      #----------------------push---------------------
      def push(self , data):
            if self.isFull():
                  return -1
            else:
                  self.__top += 1
                  self.__stack[self.__top] = data
                  return 1

      #---------------------pop----------------------
      def pop(self):
            if self.isEmpty():
                  return -1
            else:
                  print("Popped Element :: {}".format(self.__stack[self.__top]))
                  self.__stack[self.__top] = 0
                  self.__top -= 1

      #---------------------peep----------------------
      def peep(self , index):
            if index > self.__top:
                  return -1
            else:
                  count = self.__top
                  while index > 1:
                        count -= 1
                        index -= 1
                  return self.__stack[count]

      #---------------------stack_top----------------------
      def stack_top(self):
            if self.isEmpty():
                  return -1
            else:
                  return self.__stack[self.__top]

      #--------------------display-----------------------
      def display(self):
            count = self.__top
            while count != -1:
                  print(self.__stack[count] , end = ' ')
                  count -= 1
            print()


#----------------------MAIN---------------------
if __name__ == "__main__":

      stack = Stack()
      n = int(input("Enter the number of stack elements :: "))
      for i in range(n):
            data = int(input("Enter the stack element :: "))
            status = stack.push(data)
            if status == 1:
                  print("Pushed in Stack")
            else:
                  print("Stack Overflow")
      stack.display()
      
      #----------------------------------------------------------------
      status = stack.pop()
      if status == -1:
            print("Empty Stack")
      else:
            stack.display()

      #----------------------------------------------------------------
      index = int(input("Enter the index :: "))
      status = stack.peep(index)      
      if status == -1:
            print("Index Out of Bound")
      else:
            print('Peeped Element :: ',status)
      
      #----------------------------------------------------------------
      status = stack.stack_top()
      if status == -1:
            print("Empty Stack")
      else:
           print("Stack Top %d"%status)