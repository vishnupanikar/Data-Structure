#------------------------------------------------------------
max_size = 10

#------------------------------------------------------------
class Hash:

      def __init__(self):
            self.__hashset = [-1]*max_size
      
      #------------------------------------------------------------
      def insert(self,data):
            index = data % 10
            index = self.find_index(index)
            self.__hashset[index] = data

      #------------------------------------------------------------
      def display(self):
            for i in range(max_size):
                  print(i," :: ",self.__hashset[i])

      #------------------------------------------------------------
      def find_index(self,index):
            if self.__hashset[index] == -1:
                  return index
            else:
                  if index < max_size-1:
                        return self.find_index(index + 1)
                  else:
                        index = 0
                        return self.find_index(0)
      
      #------------------------------------------------------------
      def search(self,element):
            index = element % 10
            flag = 0
            while self.__hashset[index] != -1:
                  if self.__hashset[index] == element:
                        flag = 1
                        break
                  else:
                        if index < max_size-1:
                              index += 1
                        else:
                              index = 0
            
            if flag == 1:
                  print('Element Found..!')
            else:
                  print('No such element..')

#------------------------------------------------------------
if __name__ == '__main__':

      myhash = Hash()
      n = int(input('Enter Number Of Elements :: '))
      #------------------------------------------------------------
      for i in range(n):
            data = int(input('Enter Data :: '))
            myhash.insert(data)
      
      #------------------------------------------------------------
      myhash.display()

      #------------------------------------------------------------
      element = int(input('Enter the element to be found :: '))
      myhash.search(element)