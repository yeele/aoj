#-*- coding: utf-8 -*-
#https://www.pramp.com/challenge/MW75pP53wAtzNPVLPG2b
#########################################################
# CODE INSTRUCTIONS:                                    #
# 1) The method findInOrderSuccessor you're asked      #
#    to implement is located at line 30.                #
# 2) Use the helper code below to implement it.         #
# 3) In a nutshell, the helper code allows you to       #
#    to build a Binary Search Tree.                     #
# 4) Jump to line 88 to see an example for how the      #
#    helper code is used to test findInOrderSuccessor.  #
#########################################################


# A node
class Node:

    # Constructor to create a new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

    def existRight(self):
        return True if self.right is not None else False
    def existLeft(self):
        return True if self.right is not None else False

# A binary search tree
class BinarySearchTree:

    # Constructor to create a new BST
    def __init__(self):
        self.root = None

    def find_smallest(self, node: Node):
        if node.left == None: return node
        elif node.left != None: return self.find_smallest(node.left)
        else: return self.find_smallest(node.right)

    def find_in_order_successor(self, inputNode: Node):
        if inputNode.existRight():
            # find smallest from sub tree
            cur:Node = inputNode.right
            if cur.left is None: return cur
            else: return self.find_smallest(cur.left)
        else:
            cur:Node = inputNode
            if cur.parent.parent == None: return None
            while cur.parent.right == cur:
                cur = cur.parent
            return cur.parent

    # Given a binary search tree and a number, inserts a
    # new node with the given number in the correct place
    # in the tree. Returns the new root pointer which the
    # caller should then use(the standard trick to avoid
    # using reference parameters)
    def insert(self, key):

        # 1) If tree is empty, create the root
        if (self.root is None):
            self.root = Node(key)
            return

        # 2) Otherwise, create a node with the key
        #    and traverse down the tree to find where to
        #    to insert the new node
        currentNode = self.root
        newNode = Node(key)
        while(currentNode is not None):

            if(key < currentNode.key):
                if(currentNode.left is None):
                    currentNode.left = newNode;
                    newNode.parent = currentNode;
                    break
                else:
                    currentNode = currentNode.left;
            else:
                if(currentNode.right is None):
                    currentNode.right = newNode;
                    newNode.parent = currentNode;
                    break
                else:
                    currentNode = currentNode.right;

    # Return a reference to a node in the BST by its key.
    # Use this method when you need a node to test your
    # findInOrderSuccessor function on
    def getNodeByKey(self, key):

        currentNode = self.root
        while(currentNode is not None):
            if(key == currentNode.key):
                return currentNode

            if(key < currentNode.key):
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right

        return None

#########################################
# Driver program to test above function #
#########################################

# Create a Binary Search Tree
bst  = BinarySearchTree()
bst.insert(20)
bst.insert(9);
bst.insert(25);
bst.insert(5);
bst.insert(12);
bst.insert(11);
bst.insert(14);
#bst.insert(10);

def test(id):
    # Get a reference to the node whose key is 9
    test = bst.getNodeByKey(id)

    # Find the in order successor of test
    succ = bst.find_in_order_successor(test)

    # Print the key of the successor node
    if succ is not None:
        print ("Inorder Successor of %d is %d " \
               %(test.key , succ.key))
    else:
        print ("Inorder Successor doesn't exist")

test(9)
test(14)
test(12)
test(20)
test(25)

def find_smallest_test(id):
    test_node = bst.getNodeByKey(id)
    ret_node = bst.find_smallest(test_node)
    if ret_node is not None:
        print ("smallest in the tree of %d is %d " %(test_node.key , ret_node.key))
    else:
        print ("smallest node doesn't exist")


# find_smallest_test(9)
# find_smallest_test(14)
# find_smallest_test(12)