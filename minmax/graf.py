#!/bin/bash

class Node:
    def __init__(self, parent, value):
        self.parent = parent
        self.children = []
        self.value = value
    
    def getGraphList(self):
        valueList = []

        for el in self.getLastNodes():
            values = []
            el.getParentNodesValues(values)
            valueList.append(values[::-1])
        
        return valueList
    
    def getParentNodesValues(self, nodes):
        if self.parent == None:
            nodes.append(self.value)
        else:
            nodes.append(self.value)
            self.parent.getParentNodesValues(nodes)
    
    def getLastNodes(self):
        nodes = []
        self._getLastNodes(nodes)
        return nodes

    def _getLastNodes(self, nodes):
        if len(self.children) == 0:
            nodes.append(self)
        else:
            for el in self.children:
                el._getLastNodes(nodes)

    def addChildren(self):
        if self.getSum() < 21:
           for el in range(4, 7):
               newNode = Node(self, el)
               newNode.addChildren()
               self.children.append(newNode)
    
    def getSum(self):
        if self.parent == None:
            return self.value
        else:
            return self.parent.getSum() + self.value
    
    def getValue(self):
        return self.value

def run():
    for el in range(4, 7):
        startPoint = Node(None, el)
        startPoint.addChildren()
        values = startPoint.getGraphList()
        for value in values:
            print(value)

if __name__ == "__main__":
    run()
