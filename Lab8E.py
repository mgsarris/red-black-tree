import csv
import time

class Tree:
    root = None
    nodeCount = 0
    parent = None
    nil = None

class Node:
    def __init__(self, left, UPC, sizeOrType, description, right, parent, color):
        self.left = None
        self.UPC = UPC
        self.sizeOrType = sizeOrType
        self.description = description
        self.right = None
        self.parent = None
        self.color = False
        Tree.nodeCount += 1


def main():
    Tree.nil = Node(None,None,None,None,None,None,False)
    Tree.root = Tree.nil
    Tree.nodeCount -= 1

    # building BST
    startTimeBuild = time.perf_counter()
    with open('UPC-random.csv', newline='') as csvfile:
        itemReader = csv.reader(csvfile, delimiter=',')
        for row in itemReader:
            RBInsert(Tree,Node(None,int(row[0]),row[1],row[2],None,None,False))
    totalTimeBuild = time.perf_counter() - startTimeBuild
    
    print("Number of nodes in Red-Black Tree:",Tree.nodeCount)
    # inOrderTreeWalk(Tree.root)

    # searching with input.dat
    startTimeSearch = time.perf_counter()
    with open('input.dat', newline='') as inputFile:
        itemReader = csv.reader(inputFile, delimiter=',')
        for row in itemReader:
            print(treeSearch(Tree.root,int(row[0])))
    totalTimeSearch = time.perf_counter() - startTimeSearch

    print("Build time took", totalTimeBuild)
    print("Search time took", totalTimeSearch)
    print("Total time", totalTimeBuild + totalTimeSearch)

def RBInsert(Tree,z):
    #currentUPC()
    y = Tree.nil
    x = Tree.root

    while x != Tree.nil:
        y = x
        if z.UPC < x.UPC:
            x = x.left
        else: 
            x = x.right

    z.parent = y

    if y == Tree.nil:
        Tree.root = z
    elif z.UPC < y.UPC:
        y.left = z
    else:
        y.right = z

    z.left = Tree.nil
    z.right = Tree.nil
    z.color = True

    RBInsertFixup(Tree,z)

def inOrderTreeWalk(x):
    if x != Tree.nil:
        inOrderTreeWalk(x.left)
        print(x.UPC)
        inOrderTreeWalk(x.right)

def leftRotate(T,x):
    y = x.right
    x.right = y.left
    if y.left != T.nil:
        y.left.parent = x
    y.parent = x.parent
    if x.parent == T.nil:
        T.root = y
    elif x == x.parent.left:
        x.parent.left = y
    else:
        x.parent.right = y
    y.left = x
    x.parent = y

def rightRotate(T,x):
    y = x.left
    x.left = y.right
    if y.right != T.nil:
        y.right.parent = x
    y.parent = x.parent
    if x.parent == T.nil:
        T.root = y
    elif x == x.parent.right:
        x.parent.right = y
    else:
        x.parent.left = y
    y.right = x
    x.parent = y

def RBInsertFixup(T,z):
    while z.parent.color == True:
        if z.parent == z.parent.parent.left:
            y = z.parent.parent.right
            if y.color == True:
                z.parent.color = False
                y.color = False
                z.parent.parent.color = True
                z = z.parent.parent
            else:
                if z == z.parent.right:
                    z = z.parent
                    leftRotate(T,z)
                z.parent.color = False
                z.parent.parent.color = True
                rightRotate(T,z.parent.parent)
        else:
            y = z.parent.parent.left
            if y.color == True:
                z.parent.color = False
                y.color = False
                z.parent.parent.color = True
                z = z.parent.parent
            else: 
                if z == z.parent.left:
                    z = z.parent
                    rightRotate(T,z)
                z.parent.color = False
                z.parent.parent.color = True
                leftRotate(T,z.parent.parent)
    T.root.color = False

def treeSearch(x,k):
    if x == None or k == x.UPC :
        return x.description
    if k < x.UPC:
        return treeSearch(x.left,k)
    else:
        return treeSearch(x.right,k)

def currentUPC():
    print(Tree.nodeCount,end='\r')

main()