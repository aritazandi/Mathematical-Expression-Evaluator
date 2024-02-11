
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

def create_tree(expression: str):
    root = Node(None) 
    current_node = root
    if "(-" in expression:
        expression = expression.replace("(-","(0-")
    
    for i in range(0,len(expression)):
        char = expression[i]
        if char == '(':
            current_node.left = Node(None)
            current_node.left.parent = current_node
            current_node = current_node.left
            
        elif char == ')':
            current_node = current_node.parent
            
        elif char in operators:
            
                
            current_node.value = char
            current_node.right = Node(None)
            current_node.right.parent = current_node
            current_node = current_node.right

        elif char.isalpha() or char=="0":
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
    variables['0'] = 0
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