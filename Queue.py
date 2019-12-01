class Que:
    def __init__(self,size):
        self.__que = [None]*size
        self.size = size
        self.__front = -1
        self.__rear = 0
    
    def peek(self):
        return self.__que[self.__front]
    
    def isfull(self):
        return self.__rear == self.size
    
    def isempty(self):
        return self.__front == -1
    
    def enque(self,data):
        if not self.isfull():
            self.__que[self.__rear] = data
            self.__rear += 1
        else:
            return print('Error Full')
    
    def deque(self):
        if not self.isempty():
            self.__front += 1
            return self.__que[self.__front - 1]
        else:
            return print('Error Empty')

    def tolist(self):
        return self.__que

    def reset(self):
        self.__front = 0 
        self.__rear = 0

class CircularQue:
    def __init__(self,size):
        self.__que = [None]*size
        self.size = size
        self.__front = -1
        self.__rear = 0

    def peek(self):
        return self.__que[self.__front]

    def isfull(self):
        return self.__rear == self.__front

    def isempty(self):
        if self.__front == -1:
            return True
        else:
            self.__front == (self.__rear+1)%self.size

    def enque(self, data):
        if not self.isfull():
            if self.isempty():
                self.__front = (self.__front+1)%self.size
            self.__que[self.__rear] = data
            self.__rear = (self.__rear+1)%self.size 
        else:
            print('Error Queue Full',self.__front,self.__rear)

    def deque(self):
        if not self.isempty():
            self.__front = (self.__front+1)%self.size 
        else:
            print('Error Queue Empty ',self.__front,self.__rear)

    def tolist(self):
        return self.__que;

    def reset(self):
        self.__front = -1
        self.__rear = 0
