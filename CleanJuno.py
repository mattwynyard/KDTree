import os, csv
from collections import namedtuple
import Tkinter, tkFileDialog

import numpy as np
from sklearn.neighbors import KDTree


def main():

    root = Tkinter.Tk()
    root.withdraw()
    path = tkFileDialog.askopenfilename(parent=root)
    
    Point = namedtuple('Point', ['x', 'y', 'z'], verbose=False)
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
            p = Point(x, y, z)
            #print p.x
            points.append(p)
            
    print points[0]
    b = bbox(points)
    print b[2] - b[0]
    print b[3] - b[1]

    #print min(x)

def bbox(points):
    x, y, z = zip(*points) #unzips tuple list
    
    return [min(x), min(y), max(x), max(y)]
    

if __name__ == "__main__":
    main()
