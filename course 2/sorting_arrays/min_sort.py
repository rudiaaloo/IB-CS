class Node:
    def __init__(value, right=0, left=0):
        self.right = right
        self.left = left
        self.value = value

values = [1,2,3,4,5]
first = Node(values[0])
for value in values[1:]:
    pass

// min(values)