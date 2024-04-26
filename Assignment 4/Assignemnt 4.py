from collections import deque
class TreeNode:
    
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_average(t: TreeNode):
    if t == None:
        return []
    averages = []
    nodes_queue = deque()
    nodes_queue.append(t)
    while len(nodes_queue) != 0:
        l_sum = 0
        l_num = len(nodes_queue)
        size = l_num
        while size > 0:
            n = nodes_queue.popleft()
            l_sum = l_sum + n.val
            if n.left:
                nodes_queue.append(n.left)
            if n.right:
                nodes_queue.append(n.right)
            size -= 1
        
        averages.append(l_sum/l_num)
    return averages

def height(t: TreeNode):
    if t == None:
        return 0

    left_height = height(t.left) + 1
    right_height = height(t.right) + 1
    
    if left_height >= right_height:
        return left_height
    else:
        return right_height

def diameter(t: TreeNode):
    if t == None:
        return 0
 
    d_m = height(t.left) + 1 + height(t.right)
    ld = diameter(t.left)
    rd = diameter(t.right)
    if d_m > max(ld, rd):
        return d_m
    else:
        return max(ld, rd)

def max_element(t: TreeNode):
    if t == None:
        return float('-inf')
    if t and t.left == None and t.right == None:
        return t.val
    
    max_right = max_element(t.right)
    max_left = max_element(t.left)
    
    if max_right > t.val and max_right >= max_left:
        return max_right
    elif max_left > t.val  and max_left >= max_right:
        return max_left
    else:
        return t.val

#Preorder Function
def pre(t1):
    if t1 == None:
        return []
    l = pre(t1.left)
    r = pre(t1.right)
    return [t1.val] + l + r
def preorder(t: TreeNode):
    if t == None:
        return None
    else:
        return pre(t)

#Postorder Function
def post(t1):
    if t1 == None:
        return []
    l = post(t1.left)
    r = post(t1.right)
    return l + r + [t1.val]
def postorder(t: TreeNode):
    if t == None:
        return None
    else:
        return post(t)
        
#is_bst function uses above written max element function as well
def min_element(t: TreeNode):
    if t == None:
        return float('inf')
    if t and t.left == None and t.right == None:
        return t.val
    
    min_right = min_element(t.right)
    min_left = min_element(t.left)
    
    if min_right < t.val and min_right <= min_left:
        return min_right
    elif min_left < t.val  and min_left <= min_right:
        return min_left
    else:
        return t.val

def is_bst(t: TreeNode):
    if t == None:
        return True

    if t.left and t.val < max_element(t.left):
        return False
    elif t.right and t.val > min_element(t.right):
        return False
    else:
        if is_bst(t.left) and is_bst(t.right):
            return True
        else:
            return False
