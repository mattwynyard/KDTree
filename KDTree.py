from collections import namedtuple
#import numpy as np
from operator import itemgetter
import Tkinter, tkFileDialog
import csv, os, random
import time

def main():

##    root = Tkinter.Tk()
##    root.withdraw()
##    path = tkFileDialog.askopenfilename(parent=root)
##    root.destroy() #not working
##    
    #Point = namedtuple('Point', ['x', 'y'], verbose=False)
##    pointsF = [(1.5,9.2), (2.7,3.6), (4.2,1.3), (3.7,7.1), (5.9,4.0), (6.2,8.1), (7.4,2.4), (8.8,8.8), (7.1,9.9), (9.5,6.5)]
    pointsI = [(1, 9), (2, 3), (4, 1), (3, 7), (5, 4), (6, 8), (7, 2), (8, 8), (7, 9), (9, 6)]
 #   points = [(7, 2, 3), (9, 6, 1), (5, 4, 2), (2, 3, 9), (4, 7, 2), (8, 1, 8)]
    time_start_r = time.clock()
    points = random_points(1000000)
    time_finish_r = time.clock()
    print "random run time = " + str(time_finish_r - time_start_r) + " sec"
    #print p
##    points = []
##    with open(path, 'r') as f:
##        reader = csv.reader(f, delimiter=',')
##        next(f) #skip header
##        for line in reader:
##            #print line[0].split('\t')
##            x = float(line[0].split('\t')[7])
##            y = float(line[0].split('\t')[6])
##            z = float(line[0].split('\t')[5])
##            #print str(x) + " " + str(y) + " " + str(z)
##            p = x, y, z
##            #print p.x
##            points.append(p)
    time_start_t = time.clock()
    k = len(points[0]) 
    kd = KDTree()
    kd.build_tree(points, 0, k)
    time_finish_t = time.clock()
    print "tree build = " + str(time_finish_t - time_start_t) + " sec"   
    #print kd.inorder(kd.root)
    time_start_l = time.clock()
    print kd.getLeafCount(kd.root)
    time_finish_l = time.clock()
    print "leaf count = " + str(time_finish_l - time_start_l) + " sec"
    time_start_d = time.clock()
    count = kd.getDepth(kd.root, 0)
    time_finish_d = time.clock()
    print "find depth = " + str(time_finish_d - time_start_d) + " sec"
    print count

def random_points(n):
    points = []
    for i in range(n):
        x = round(100 * random.random(), 4)
        y = round(100 * random.random(), 4)
        z = round(100 * random.random(), 4)
        points.append((x ,y, z))
    return points

def median_index(points, axis):
    #points.sort(key=itemgetter(axis))
    #points.sort(key=lambda r:r[axis])
    #points = sorted(points, key=lambda x:x[axis])
    points = sorted(points, key=itemgetter(axis))
                    
    return len(points) / 2

class Node:

    def __init__(self):
        self.value = None
        self.left = None
        self.right = None
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
            node.value = points[i][axis] #median value for x, y or z
        if len(points) <= 5:
            node = Node()
            node.points = points
            return node
        else:
            node.value = points[i][axis]
            node.left = self.build_tree(points[:i], depth + 1, k)
            node.right = self.build_tree(points[i:], depth + 1, k)   
        return node
           
    def inorder(self, node):
        if node == None:
            return
        else:
            self.inorder(node.left)
            if node.points is not None:
                print node.points
            print node.value
            self.inorder(node.right)

##    def getLeaves(self, node):
##        if node == None:
##            return
##        else:
            

    def getDepth(self, node, count):
        if node == None:
            return 0
        if (node.left is None and node.right is None):
            return count          
        else:
            return self.getDepth(node.left, count + 1)

    def getLeafCount(self, node):
        if node is None:
            return 0
        if(node.left is None and node.right is None):
            return 1
        else:
            return self.getLeafCount(node.left) + self.getLeafCount(node.right)       
            
if __name__ == "__main__":
    main()
