#include <iostream>
 
class BinTreeNode(object): #Class for every binary tree node
 
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None
 
 
       
def tree_insert( tree, item): #function to insert each item into the binary seach tree
    
    if tree==None: 
        tree=BinTreeNode(item) 
    else:
        if(item < tree.value): #if input item is less than the current tree node..
            if(tree.left==None): #...if the node to the left is empty...
                tree.left=BinTreeNode(item) #...node for input item is created to the left of the node
            else:
                tree_insert(tree.left,item) #else call function again with node to the left
        else:
            if(tree.right==None): #else... if element to the right is empty...
                tree.right=BinTreeNode(item)#...node for input item is created to the right of he node
            else:
                tree_insert(tree.right,item)#else...call function again with the node to the right
    
    return(tree)


def in_order(tree): #takes the BST as input and traverses it to return the values in order
    stack = [] #temp stack to work with
    Thenode = tree
    solution = [] #final sorted list
    while Thenode != None or len(stack) >0:
        if Thenode != None: #if Thenode is not None, append it to the stack
            stack.append(Thenode)
            Thenode=Thenode.left #Thenode is set to node.left
        else:
            Thenode = stack.pop() #if no node to the left then node is last item in stack
            solution.append(Thenode.value) #node added to solution
            Thenode=Thenode.right
    print (solution) #print sorted list
        


def Tree_Sort(a): #function to take a list of values, create a BST and then traverse it in order.
    t=tree_insert(None,a[0]); #insert first element with none tree
    a=a[1:] 
    for i in a: #insert rest of list
        tree_insert(t,i)
        
    in_order(t)
        
    

a = (6,10,5,2,3,4,11,1) #list of values to input into the Tree_Sort function


Tree_Sort(a)



