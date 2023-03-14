class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def __r_insert(self, current_node, value):
        if current_node is None:
            return Node(value)
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)
        return current_node

    def r_insert(self, value):
        if self.root is None:
            self.root = Node(value)
        self.__r_insert(self.root, value)

    def contains(self, value):
        if self.root is None:
            return False
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

    def __r_contains(self, current_node, value):
        if current_node is None:
            return False
        if value == current_node.value:
            return True
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)

    def r_contains(self, value):
        return self.__r_contains(self.root, value)

    def __delete_node(self, current_node, value):
        if current_node is None:
            return None
        if value < current_node.value:
            current_node.left = self.__delete_node(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.__delete_node(current_node.right, value)
        else:
            if current_node.left is None and current_node.right is None:
                return None
            elif current_node.left is None:
                current_node = current_node.right
            elif current_node.right is None:
                current_node = current_node.left
            else:
                sub_tree_min = self.min_value(current_node.right)
                current_node.value = sub_tree_min
                current_node.right = self.__delete_node(current_node.right, sub_tree_min)
        return current_node

    def delete_node(self, value):
        self.__delete_node(self.root, value)

    # starts a root and searches through each node at current depth
    # before moving onto the next level of nodes
    def BFS(self):
        # set current_node to the root of the tree
        current_node = self.root

        # create an empty queue to store nodes to visit
        queue = []

        # create an empty list to store the values of visited nodes
        results = []

        # add the root node to the queue
        queue.append(current_node)

        # continue until all nodes have been visited
        while len(queue) > 0:
            # remove the first node from the queue
            current_node = queue.pop(0)

            # add the value of the visited node to the results list
            results.append(current_node.value)

            # if the visited node has a left child, add it to the queue
            if current_node.left is not None:
                queue.append(current_node.left)

            # if the visited node has a right child, add it to the queue
            if current_node.right is not None:
                queue.append(current_node.right)

        # return the list of visited node values
        return results

    # goes through entire depth of each node starting with left side
    # finishing off with right and restarting with each node-level
    def dfs_pre_order(self):
        results = []  # create an empty list to store the values of visited nodes

        def traverse(current_node):
            # append the value of the current node to the results list
            results.append(current_node.value)

            # if the current node has a left child, recursively traverse it
            if current_node.left is not None:
                traverse(current_node.left)

            # if the current node has a right child, recursively traverse it
            if current_node.right is not None:
                traverse(current_node.right)

        # start the pre-order traversal from the root of the tree
        traverse(self.root)

        # return the list of visited node values
        return results

    def dfs_post_order(self):
        results = []  # create an empty list to store the values of visited nodes

        def traverse(current_node):
            # if the current node has a left child, recursively traverse it
            if current_node.left is not None:
                traverse(current_node.left)

            # if the current node has a right child, recursively traverse it
            if current_node.right is not None:
                traverse(current_node.right)

            # append the value of the current node to the results list
            results.append(current_node.value)

        # start the post-order traversal from the root of the tree
        traverse(self.root)

        # return the list of visited node values
        return results

    def dfs_in_order(self):
        results = []  # create an empty list to store the values of visited nodes

        def traverse(current_node):
            # if the current node has a left child, recursively traverse it
            if current_node.left is not None:
                traverse(current_node.left)

            # append the value of the current node to the results list
            results.append(current_node.value)

            # if the current node has a right child, recursively traverse it
            if current_node.right is not None:
                traverse(current_node.right)

        # start the in-order traversal from the root of the tree
        traverse(self.root)

        # return the list of visited node values
        return results

    def min_value(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value


my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print(my_tree.dfs_pre_order())
