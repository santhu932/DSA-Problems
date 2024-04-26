import collections
#Problem 1

def postfix_string(arr):
    if len(arr) == 0:
        return None
    st = []
    for i in range(len(arr)):
        if str(arr[i]) != '+' and str(arr[i]) != '-' and str(arr[i]) != '*':
            st.append(arr[i])
        # implemets the mentioned concatenation operation for +
        if arr[i] == '+':
            if len(st) > 1 :
                s = st.pop()
                f = st.pop()
                st.append(f + s)
        # implements the mentioned removal operation for -
        if arr[i] == '-':
            if len(st) > 1:
                s = st.pop()
                f = st.pop()
                st.append(f[:int(s)] + f[int(s)+1:])
        # implements the mentioned repeatation operation for *
        if arr[i] == '*':
            if len(st) > 1:
                s = st.pop()
                f = st.pop()
                st.append(f * int(s))
    result = st.pop()        
    return result

#Problem 2

class ListNode():
      def __init__(self, val, next=None):
            self.val = val
            self.next = next

class AstronomicalInt():
    
    # function to insert new node in the linked list
    def insert(self, head, element):
        node = ListNode(element)
        if head == None:
            head = node
        else:
            p = head
            while p.next != None:
                p = p.next
            p.next = node
        return head
    
    #function to reverse the linked list
    def reverse(self, head):
        if head == None or head.next == None:
            return head
        present = head
        back = None
        front = None
        while present != None:
            front = present.next
            present.next = back
            back = present
            present = front
        head = back
        return head
    
    def convert(self, num:str):
        if num == '':
            return None
        head = None
        #Converts string to linked list
        for k in range(len(num)):
            head = self.insert(head, num[k])
        return head
            
    def add(self, num1:ListNode, num2: ListNode):
        if num1 == None:
            return num2
        if num2 == None:
            return num1
        # Reverse two linked lists to perform addition operation
        num1 = self.reverse(num1)
        num2 = self.reverse(num2)
        result = None
        last = None
        s = 0
        c = 0 #carry
        
        while num1 != None or num2 != None:
            if num1 != None:
                data1 = int(num1.val)
            else:
                data1 = 0
                
            if num2 != None:
                data2 = int(num2.val)
            else:
                data2 = 0
                
            s = data1 + data2 + c
            #Adding carry
            if s >= 10:
                c = 1
            else:
                c = 0
            
            s = s % 10

            node = ListNode(s)
            if result == None:
                result = node
            else:
                last.next = node
            last = node
            
            if num1 != None:
                num1 = num1.next
            if num2 != None:
                num2 = num2.next
        #inserting carry node  
        if c > 0:
            last.next = ListNode(c)

        result = self.reverse(result)
        return result

    def to_string(self, head):
        num = []
        curr = head
        while curr:
            num.append(curr.val)
            curr = curr.next
        num = ''.join([str(i) for i in num])
        return num
#Problem 3

def countAtoms(formula):
    size = len(formula)
    #Creating the stack list of dict counters to maintain the count of an element
    stk = [collections.Counter()]
    c = 0
    while c < size:
        #Adding the elemnts to the stack
        if formula[c] == '(':
            stk.append(collections.Counter())
            c = c + 1
        #Adding the counts for the elements within brackets
        elif formula[c] == ')':
            element = stk.pop()
            c = c+1
            k = c
            while c < size and formula[c].isdigit():
                c = c + 1
            if formula[k:c] != '':
                factor = int(formula[k:c])
            else:
                factor = 1
            for k, v in element.items():
                stk[-1][k] = stk[-1][k] + (v*factor)
        #Adding counts to elements where digits are followed by the alpha characters
        else:
            k = c
            c = c+ 1
            while c < size and formula[c].islower():
                c = c+1
            element1 = formula[k:c]
            k = c
            while c < size and formula[c].isdigit():
                c = c + 1
            if formula[k:c] != '':
                factor = int(formula[k:c])
            else:
                factor = 1
            stk[-1][element1] = stk[-1][element1] + factor
    #Merging the elements with their counts in sorted order
    string = ""
    for element in sorted(stk[-1]):
        if stk[-1][element] > 1:
            string = string + element + str(stk[-1][element])
        else:
            string = string + element + ''
            
    return string
    
#Problem 4
def combination_check(n,st):
    number = str(n)
    words = st.split()
    match_dict = dict() #To match the digit to the word
    w = [] #To keep track of visited words
    #Checking size of both total number digits and number of words
    if len(number) != len(words):
        return False
    #Iterating over the digits and updating words in the dict accordingly, if there is incorrect match then returns false
    for m in range(len(words)):
        if number[m] not in match_dict:
            if words[m] not in w:
                match_dict[number[m]] = words[m]
                w.append(words[m])
            else:
                return False
        else:
            if words[m] != match_dict[number[m]]:
                return False
    return True
    
#Problem 5

def diff_max_min(arr):
    if len(arr) == 0:
        return None
    size = len(arr)
    stack = []
    right = [None] * size #To store number of elements that are present between the current element and next greater or lesser element on its right side 
    left = [None] * size #To store number of elements that are present between the current element and next greater or lesser element on its left side
    #Stores the worst case values, in case if we don't the elements on its right or left side
    for k in range(len(arr)):
        right[k] = (size - 1) - k 
        left[k] = k
    #Finding the number of elements within next minimum number on the right side
    for j in range(size):
        while len(stack) != 0 and arr[stack[len(stack)-1]] > arr[j]:
            right[stack[len(stack)-1]] = j - stack[len(stack)-1] - 1
            stack.pop()
        stack.append(j)
    k = size - 1
    stack = []
    #Finding the number of elements within next minimum number on the left side
    while k >= 0:
        while len(stack) != 0 and arr[stack[len(stack)-1]] >= arr[k]:
            left[stack[len(stack)-1]] = stack[len(stack)-1] - k -1
            stack.pop()
        stack.append(k)
        k -= 1
    min_sum = 0
    #Calculating the sum of Minimum element of all the subarrays, given by following formulation
    for k in range(size):
        min_sum += arr[k] * ((right[k] + 1) * (left[k] + 1))
      
    
    stack = []
    right = [None] * size
    left = [None] * size
    #Stores the worst case values, in case if we don't the elements on its right or left side
    for k in range(len(arr)):
        right[k] = (size - 1) - k
        left[k] = k
    #Finding the number of elements within next maximum number on the right side
    for j in range(size):
        while len(stack) != 0 and arr[stack[len(stack)-1]] <= arr[j]:
            right[stack[len(stack)-1]] = j - stack[len(stack)-1] - 1
            stack.pop()
        stack.append(j)
    k = size - 1
    stack = []
    #Finding the number of elements within next maximum number on the left side
    while k >= 0:
        while len(stack) != 0  and arr[stack[len(stack)-1]] < arr[k]:
            left[stack[len(stack)-1]] = stack[len(stack)-1] - k -1
            stack.pop()
        stack.append(k)
        k -= 1
    #Calculating the sum of Maximum element of all the subarrays, given by following formulation
    max_sum = 0
    for k in range(size):
        max_sum += arr[k] * ((right[k] + 1) * (left[k] + 1))
    #Calculation the difference   
    difference_max_min = max_sum - min_sum
            
    return difference_max_min


 

