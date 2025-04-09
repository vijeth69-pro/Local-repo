class node:
    __value=None
    __next=None

    def __init__(self):
        self.__value=eval(input('Enter value for the node:'))
        self.__next=None

    def get_value(self):
        return self.__value

    def set_value(self,v):
        self.__value=v

    def get_next(self):
        return self.__next
    
    def set_next(self,n):
        self.__next=n

class sll:
    __head=None
    __current=None

    def __init__(self):
        self.__head=None

    def get_head(self):
        return(self.__head)
    
    def set_head(self,n):
        self.__head=n

    def prepend_list(self):
        n=node()
        n.set_next(self.__head)
        self.__head=n
        
    def remove_beg(self):
        if self.__head==None:
            print("List empty cannot remove")
        else:
            n=self.__head
            self.__head=n.get_next()
            n.set_next(None)
            print(n.get_value(),"removed from the begining")
                    
    def display_list(self):
        if self.__head==None:
            print("List is empty")
        else:
            self.__current=self.__head
            while self.__current.get_next()!=None:
                print(self.__current.get_value())
                self.__current=self.__current.get_next()
            print(self.__current.get_value())

    def __iter__(self):
        self.__current=self.__head
        return(self)
       
    def __next__(self):
        if self.__current==None:
            raise StopIteration
        else:
            n=self.__current
            self.__current=self.__current.get_next()
            return n.get_value()

if __name__ == "__main__":
        my_list=sll()
        while True:
            print("1:Execute Prepend list\n2:Execute remove begining\n3:Display list using function\n4:Display list using Iteration\n5:exit\n")
            op=int(input("Enter your choice:"))
            if op==1:
                my_list.prepend_list()
            elif op==2:
                my_list.remove_beg()
            elif op==3:
                my_list.display_list()
            elif op==4:
                for i in my_list:
                    print(i)
            elif op==5:
                print("Thank you")
                break
            else:
                print("Invalid choice")
