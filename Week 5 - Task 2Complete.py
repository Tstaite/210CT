class Node(object):
    def __init__(self, value):
        self.value=value
        self.next=None
        self.prev=None

class List(object):
    def __init__(self):
        self.head=None
        self.tail=None
    def insert(self,n,x):
        if n!=None:
            x.next=n.next
            n.next=x
            x.prev=n
            if x.next!=None:
                x.next.prev=x              

        if self.head==None:
            self.head=self.tail=x
            x.prev=x.next=None
        elif self.tail==n:
            self.tail=x
    def display(self):
        values=[]
        n=self.head
        
        while n!=None:
            values.append(str(n.value))
            n=n.next
        print ("List: ",",".join(values))
        

    #function to delete node from linked list
    def delete(self, Node):
        start=self.head #starts at first element in list
        i = 1
        while i < Node:
            start=start.next #finds node to be deleted
            i=i+1
        #if not head item, link previous element to next element
        if start.prev != None:
            start.prev.next = start.next
        #else, head item becomes second item
        else:
            self.head = start.next
        #if not tail item, next items previous item, becomes previous item
        if start.next != None:
            start.next.prev = start.prev
        #else, tail item becomes previous item
        else:
            self.tail = start.prev
        

        
          
if __name__ == '__main__':
    l=List()
    l.insert(None, Node(4))
    l.insert(l.head,Node(6))
    l.insert(l.head,Node(8))
    l.insert(l.head,Node(5))
    l.insert(l.head,Node(7))
    l.insert(l.head,Node(2))
    


    
    l.display()
    l.delete(6)
    l.display()
    
    



