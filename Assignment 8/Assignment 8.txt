# Problem 1

class MaxHeap:
    def __init__(self, ls=None):
        self.heap = ls
        self.heapify(0)
  
    def heapify(self, index):
        old_i = index
        #Checking heap property with left child
        if (2 * old_i + 1) < len(self.heap) and self.heap[index] < self.heap[2 * old_i + 1]:
            index = 2 * old_i + 1
        #Checking heap property with right child
        if (2 * old_i + 2) < len(self.heap) and self.heap[index] < self.heap[2 * old_i + 2]:
            index = 2 * old_i + 2
        #Swap operation and heapify recursively
        if index != old_i:
            value = self.heap[old_i]
            self.heap[old_i] = self.heap[index]
            self.heap[index] = value
            self.heapify(index)
            
    def insert(self, element):
        #inserting element on right most leaf node level
        self.heap.append(element)
        k = len(self.heap) - 1
        #Checking heap property from leaf node (inserted element) to root by swaping nodes if needed
        while k > 0 and self.heap[(k-1)//2] < self.heap[k]:
            value = self.heap[k]
            self.heap[k] = self.heap[(k-1)//2]
            self.heap[(k-1)//2] = value
            k = (k-1)//2
       

    def getMax(self):
        if len(self.heap) == 0:
            return None
        m_val = self.heap[0]
        self.heap[0] = self.heap[len(self.heap) - 1]
        #deleting the element from leaf level after swap
        del self.heap[len(self.heap) - 1]
        self.heapify(0)
        return m_val

    def print(self):
        return self.heap

    
def test_max_heap(input):
    mx = None
    result = []
    i = 0
    while i < len(input):
        if input[i] == 'MaxHeap':
            mx = MaxHeap(input[i+1])
            result.append(None)
            i += 2
        elif input[i] == 'insert':
            result.append(mx.insert(input[i+1]))
            i += 2
        elif input[i] == 'getMax':
            result.append(mx.getMax())
            i += 1
        elif input[i] == 'print':
            res = mx.print()
            result.append(res[:])
            i += 1
        else:
            i += 1
    return result 

# Problem 2 and 3

import heapq

class node:
    def __init__(self, count, symbol, lchild=None, rchild=None):
        self.symbol = symbol
        self.count = count
        self.lchild = lchild
        self.rchild = rchild
        self.code = ''
        
    def __lt__(self, next):
        #Comparing nodes based on counts
        if self.count != next.count or self.symbol == None or next.symbol == None:
            return self.count < next.count
        else:
            return ord(self.symbol) < ord(next.symbol) #Comparing based on characters if the counts are same
        
class HuffmanCoding:
    
    
    def encode(self, s):
        
        #Creating frequency dictionary
        f_count = dict()
        for c in s:
            if c in f_count:
                f_count[c] += 1
            else:
                f_count[c] = 1

        #Creating heap array    
        heap_array = []
        for c, f in f_count.items():
            heap_array.append(node(f, c))
        heapq.heapify(heap_array)
        
        #Huffman Coding algorithm
        while len(heap_array) > 1:
            left_child = heapq.heappop(heap_array)
            left_child.code = '0'
            right_child = heapq.heappop(heap_array)
            right_child.code = '1'
            combined_count = left_child.count + right_child.count
            combined_node = node(combined_count, None, left_child, right_child)
            heapq.heappush(heap_array, combined_node)
        
        #Creating character-code dictionary
        codes = dict()
        st = [(heap_array[0], '')]
        while st:
            n, code = st.pop()
            if n.symbol:
                codes[n.symbol] = code + n.code
            if n.lchild:
                st.append((n.lchild, code + n.code))
            if n.rchild:
                st.append((n.rchild, code + n.code))
        
        #Encoding message using character-code dictionary
        encoded_msg = ''
        for c in s:
            encoded_msg = encoded_msg + codes[c]
            
        #Ordering the dictionary based on characters
        char_list = list(codes.keys())
        char_list.sort()
        ordered_codes = {c: codes[c] for c in char_list}

        return encoded_msg, ordered_codes
    
        
  
    
    def decode(self, s, d):

        #Creating code-character dictionary
        code_dict = dict()
        for k, v in d.items():
            code_dict[v] = k

        #Decoding message using code-character dictionary
        decoded_msg = ''
        c = ''
        for b in s:
            c = c + b
            if c in code_dict:
                decoded_msg = decoded_msg + code_dict[c]
                c = ''
        
        return decoded_msg