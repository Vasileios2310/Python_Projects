class Node:
    def __init__(self , value):
        self._value = value # save the value of Node (private)
        self._children = [] # list with all children of Node (private)
        
    def __repr__(self):
        """special method that returns a string representation of an object"""
        return 'Node{!r}'.format(self._value)
    
    def add_child(self,node):
        self._children.append(node)
        
    def __iter__(self):
        """
        Returns: an iterator for list self._children
        """
        return iter(self._children)
    
if __name__ == '__main':
    """
        root --> object of Class Node
        Node is iterable object
        __iter__ is called
    """
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    # for ch in root.__iter__:
    for ch in root:
        print(ch)
