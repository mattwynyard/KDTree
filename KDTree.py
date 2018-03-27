from collections import namedtuple
import numpy as np
from operator import itemgetter
import Tkinter, tkFileDialog
import csv, os

def main():

    root = Tkinter.Tk()
    root.withdraw()
    path = tkFileDialog.askopenfilename(parent=root)
    root.destroy() #not working
    
    #Point = namedtuple('Point', ['x', 'y'], verbose=False)
##    pointsF = [(1.5,9.2), (2.7,3.6), (4.2,1.3), (3.7,7.1), (5.9,4.0), (6.2,8.1), (7.4,2.4), (8.8,8.8), (7.1,9.9), (9.5,6.5)]
##    pointsI = [(1, 9), (2, 3), (4, 1), (3, 7), (5, 4), (6, 8), (7, 2), (8, 8), (7, 9), (9, 6)]
##    pointsA = [(7, 2), (9, 6), (5, 4), (2, 3), (4, 7), (8, 1)]

    points = []
    with open(path, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        next(f) #skip header
        for line in reader:
            #print line[0].split('\t')
            x = float(line[0].split('\t')[7])
            y = float(line[0].split('\t')[6])
            z = float(line[0].split('\t')[5])
            #print str(x) + " " + str(y) + " " + str(z)
            p = x, y, z
            #print p.x
            points.append(p)
    k = len(points[0]) - 1
    #print k
    kd = KDTree()
    kd.build_tree(points, 0, k)
    #print kd.inorder(kd.root)
    print kd.getLeafCount(kd.root)

def median_index(points, axis):
    points.sort(key=itemgetter(axis))
    return len(points) / 2

class Node:

    def __init__(self, value=None):
        if value is not None:
            self.value = value
        self.value = None
        self.left = None
        self.right = None
        self.depth = None
        self.points = None

    def __str__(self):
        return str(self.value)

class KDTree:
    
    def __init__(self):
        self.root = None

    def build_tree(self, points, depth, k):
        axis = depth % k
        i = median_index(points, axis)
        #print points

        node = Node()
        if self.root == None:
            self.root = node
 #           node.points = points
            node.value = points[i][axis]
        if len(points) <= 16:
            node = Node()
            node.points = points
 #           node.value = points[i][axis]
            return node
        else:
 #           node.points = points
            node.value = points[i][axis]
            node.left = self.build_tree(points[:i], depth + 1, k)
            node.right = self.build_tree(points[i:], depth + 1, k)
    
        return node
           
    def inorder(self, node):
        if node == None:
            return
        else:
            self.inorder(node.left)
            print node.points
            print node.value
            self.inorder(node.right)

    def getLeafCount(self, node):
        if node is None:
            return 0
        if(node.left is None and node.right is None):
            return 1
        else:
            return self.getLeafCount(node.left) + self.getLeafCount(node.right)

        

class BST:
  
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value <= node.value:
            if node.left == None:
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        elif value > node.value:
            if node.right == None:
                node.right = Node(value)
            else:
                self._insert(node.right, value)


    def inorder(self, node):
        if node == None:
            return
        else:
            self.inorder(node.left)
            print node.value
            self.inorder(node.right)
        
            
if __name__ == "__main__":
    main()
