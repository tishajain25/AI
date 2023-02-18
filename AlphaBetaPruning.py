# Code of working of Alpha Beta Pruning

import math

class Node:
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children

def alpha_beta_minimax(node, depth, alpha, beta, maximizingPlayer, evaluate):
    if depth == 0 or len(node.children) == 0:
        return evaluate(node)
    
    if maximizingPlayer:
        v = -math.inf
        for child in node.children:
            v = max(v, alpha_beta_minimax(child, depth-1, alpha, beta, False, evaluate))
            alpha = max(alpha, v)
            if beta <= alpha:
                break
        return v
    else:
        v = math.inf
        for child in node.children:
            v = min(v, alpha_beta_minimax(child, depth-1, alpha, beta, True, evaluate))
            beta = min(beta, v)
            if beta <= alpha:
                break
        return v
        
# For Example
A = Node(3, [
        Node(5, [Node(2), Node(8)]),
        Node(2, [Node(6), Node(7)]),
        Node(4, [Node(1), Node(3)])
    ])

def evaluate(node):
    return node.value

alpha = -math.inf
beta = math.inf
depth = 3
score = alpha_beta_minimax(A, depth, alpha, beta, True, evaluate)
print("The optimal value is:", score)
