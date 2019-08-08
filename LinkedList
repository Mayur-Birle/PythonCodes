# Node Class
class Node:
    def __init__(self,data):
        self.__data = data;
        self.__next = None;

    def set_data(self,data):
        self.data = data;

    def set_next(self,next):
        self.__next = next;

    def get_data(self):
        return self.__data;

    def get_next(self):
        return self.__next;
        
# LinkedList Class
class LinkedList:
    def __init__(self):
        self.__head = None;
        self.__tail = None;

    def get_head(self):
        return self.__head;

    def get_tail(self):
        return self.__tail;
        
    def add(self,data):
        temp = self.__tail;
        if(temp == None):
            self.__head = self.__tail = Node(data);
        else:
            temp.set_next(Node(data));
            self.__tail = temp.get_next();
            
    def display(self):
        temp = self.__head;
        while(temp!=None):
            print(temp.get_data(),end=" ");
            temp = temp.get_next();
        print();

    def find_node(self,data):
        temp = self.__head;
        postion = 0
        while(temp!=None):
            if(temp.get_data() == data):
                return postion;
            temp = temp.get_next();
            postion += 1;
        return False;

    def get_node(self, postion):
        temp = self.__head;
        for i in range(postion):
            temp = temp.get_next();
        return temp;

    def insert_at(self,data,postion):
        temp = self.__head;
        if(postion == 0):
            n = Node(data);
            n.set_next(temp);
            self.__head = n;
            return;
        for _ in range(postion-1):
            temp = temp.get_next();
        n = Node(data);
        n.set_next(temp.get_next());
        temp.set_next(n);

    def delete_at(self,postion):
        temp = self.__head;
        if(postion == 0):
            self.__head = self.__head.get_next();
            del temp;
            return;
        for _ in range(postion-1):
            temp = temp.get_next();
        n = temp.get_next().get_next();
        x = temp.get_next()
        del x;
        temp.set_next(n);

list = LinkedList()
list.add(1)
list.add(51)
list.add(81)
list.add(18)
list.add(15)
list.insert_at(90,0)
list.insert_at(40,4)
list.delete_at(5)
list.delete_at(0)
list.display();
