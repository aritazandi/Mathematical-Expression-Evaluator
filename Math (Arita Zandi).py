
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

def create_tree(expression):
    root = Node(None) 
    current_node = root
    
    for i in range(0,len(expression)):
        char = expression[i]
        if char == '(':
            current_node.left = Node(None)
            current_node.left.parent = current_node
            current_node = current_node.left
            
        elif char == ')':
            current_node = current_node.parent
            
        elif char in operators:
            
            if expression[i-1] == '(':
                current_node.left = Node(0)
                current_node.left.parent = current_node
                
            current_node.value = char
            current_node.right = Node(None)
            current_node.right.parent = current_node
            current_node = current_node.right

        elif char.isalpha():
            current_node.value = char
            current_node = current_node.parent

    return root  

postfix = []
def post_order(node):
    if node is not None:
        post_order(node.left)
        post_order(node.right)
        if node.value is not None:
            postfix.append(node.value)

def evaluate_postfix(postfix, variables):
    stack = []
    
    for char in postfix:
        if char in operators:

            qabli = stack.pop()
            qabl_qabli = stack.pop()
            
            if char == '+':
                stack.append(qabl_qabli + qabli)
            elif char == '-':
                stack.append(qabl_qabli - qabli)
            elif char == '*':
                stack.append(qabl_qabli * qabli)
            elif char == '/':
                stack.append(qabl_qabli / qabli)
            elif char == '^':
                stack.append(qabl_qabli ** qabli)
            
        else:
            if char == 0:
                stack.append(0)
            else:
                stack.append(variables[char])
                
    return stack.pop()

operators = {'+', '-', '*', '/', '^'}
expression = "(((a+b)+(c*a))^(-a))"
variables = {'a': -1, 'b': 2, 'c': 3}

tree_root = create_tree(expression)

post_order(tree_root)
print(expression)
print(f"postfix: {postfix}")
print(variables)

result = evaluate_postfix(postfix, variables)
print(f"The result is {result}")