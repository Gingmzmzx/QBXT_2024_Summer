class Node:
    def __init__(self):
        self.children = {}
        self.failure = None
        self.patterns = []

class AC:
    def __init__(self):
        self.root = Node()

    def add_pattern(self, pattern):
        node = self.root
        for char in pattern:
            if char not in node.children:
                node.children[char] = Node()
            node = node.children[char]
        node.patterns.append(pattern)

    def build_failure(self):
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            for char, child in node.children.items():
                if node == self.root:
                    child.failure = self.root
                else:
                    fail_node = node.failure
                    while fail_node and char not in fail_node.children:
                        fail_node = fail_node.failure
                    if fail_node:
                        child.failure = fail_node.children[char]
                    else:
                        child.failure = self.root
                queue.append(child)

    def match(self, text):
        node = self.root
        for i, char in enumerate(text):
            while node and char not in node.children:
                node = node.failure
            if node:
                node = node.children[char]
                if node.patterns:
                    return True
        return False

def check_string(str1, lists):
    ac = AC()
    for string in lists:
        ac.add_pattern(string)
    ac.build_failure()
    return ac.match(str1)