#--------------------------Max Queue size---------------------------
max_size = 10

#---------------------------Queue Class----------------------------
class Queue:
      def __init__(self):
            self.__front = -1
            self.__rear = -1
            self.__queue = [0]*max_size

#--------------------------isFull()-----------------------------
      def isFull(self):
            if self.__rear+1 == max_size:
                  return True
            else:
                  return False

#---------------------------isEmpty()----------------------------
      def isEmpty(self):
            if self.__front == self.__rear:
                  return True
            else:
                  return False

#-----------------------------enqueue()--------------------------
      def enqueue(self , data):
            if self.isFull():
                  return -1
            else:
                  if self.__front == -1:
                        self.__front += 1
                        self.__rear += 1
                  else:
                        self.__rear += 1
                  
                  self.__queue[self.__rear] = data

#---------------------------display()----------------------------
      def display(self):
            index = self.__front
            while(index <= self.__rear):
                  print(self.__queue[index] , end=' ')
                  index += 1
            print()

#---------------------------dequeue()----------------------------
      def dequeue(self):
            if self.isEmpty() : 
                  return -1
            else:
                  value = self.__queue[self.__front]
                  index = self.__front
                  while(index < self.__rear):
                        self.__queue[index] = self.__queue[index+1]
                        index += 1
                  
                  if self.__front == self.__rear:
                        self.__front -= 1
                        self.__rear -= 1
                  else:
                        self.__rear -= 1
                  return value

#---------------------------MAIN----------------------------
if __name__ == '__main__':
      myqueue = Queue()

      #-------------------------------------------------------
      size = int(input('Enter size of queue :: '))
      for i in range(size):
            data = int(input('Enter data :: '))
            status = myqueue.enqueue(data)
            if status == -1:
                  print("Queue is Full")
            else:
                  print("Entered in queue...")
      
      myqueue.display()

      #-------------------------------------------------------
      status = myqueue.dequeue()
      if status == -1:
            print("Queue is Empty")
      else:
            print("Removed From Queue :: ",status)

      myqueue.display()