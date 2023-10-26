from dataclasses import dataclass
from typing import Any

# The BstMap class is a binary search tree based implementation of
# a map (or dictionary). It works for any type of values and for
# all types keys that are comparable ==> we can compare keys using
# the operators < and >.


# The Node class is responsible for most of the work.
# Each call to the BstMap class is just delegated to the
# root node which starts a recursive sequence of calls to
# handle the request. Notice: All Node methods are recursive.
@dataclass
class Node:
    key: Any = None         # the key
    value: Any = None       # the value
    left: Any = None        # left child (a Node)
    right: Any = None       # right child (a Node)

    def put(self, key, value):
        # if new key is less than old key go left
        if key < self.key:
            if self.left is None:               # if no left child
                self.left = Node(key, value)    # create new left child
            else:
                # recursively call put on the left child
                self.left.put(key, value)
        elif key > self.key:
            # if new key is greater than old go right
            if self.right is None:              # if no right child
                self.right = Node(key, value)   # create a new right child
            else:
                # Otherwise, recursively call put on the right child
                self.right.put(key, value)
        else:
            # If the key already exists, update the value
            self.value = value

    def contains(self, key):
        return self.get(key) is not None

    def inorder_traversal(self):
        result = []
        if self.left is not None:
            result.extend(self.left.inorder_traversal())
        result.append((self.key, self.value))
        if self.right is not None:
            result.extend(self.right.inorder_traversal())
        return result

    def to_string(self):
        pass

    def count(self):
        pass

    def get(self, key):
        if key == self.key:
            return self.value
        elif key < self.key and self.left is not None:
            return self.left.get(key)
        elif key > self.key and self.right is not None:
            return self.right.get(key)
        return None

    def max_depth(self):
        pass

    def count_internal_nodes(self):
        pass

    # We do a left-to-right in-order traversal of the tree
    # to get the key-value pairs sorted base on their keys
    def as_list(self, lst):
        pass


# The BstMap class is rather simple. It basically just takes care
# of the case when the map is empty. All other cases are delegated
# to the root node ==> the Node class.
@dataclass
class BstMap:
    root: Node = None

    # Adds a key-value pair to the map
    def put(self, key, value):
        if self.root is None:    # Empty, add first node
            self.root = Node(key, value, None, None)
        else:
            self.root.put(key, value)

    # Returns a string representation of all the key-value pairs
    def to_string(self):
        if self.root is None:     # Empty, return empty brackets
            return "{ }"
        else:
            res = "{ "
            res += self.root.to_string()
            res += "}"
            return res

    # Returns the current number of key-value pairs in the map
    def size(self):
        if self.root is None:
            return 0
        else:
            return self.root.count()

    # Returns the value for a given key. Returns None
    # if key doesn't exist (or map is empty)
    def get(self, key):
        if self.root is None:
            return None
        else:
            return self.root.get(key)

    # Returns the maximum tree depth. That is, the length
    # (counted in nodes) of the longest root-to-leaf path
    def max_depth(self):
        if self.root is None:
            return 0
        else:
            return self.root.max_depth()

    # Returns an internal node count. That is, the number of nodes 
    # that has aleast one child (i.e. not leafs)
    def count_internal_nodes(self):
        if self.root is None:
            return 0
        else:
            return self.root.count_internal_nodes()

    # Returns a sorted list of all key-value pairs in the map.
    # Each key-value pair is represented as a tuple and the
    # list is sorted on the keys ==> left-to-right in-order
    def as_list(self):
        lst = []
        if self.root is None:
            return lst
        else:
            return self.root.as_list(lst)
