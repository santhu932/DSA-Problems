import random

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.down = None

class LookUpSkipList:
    def __init__(self, probability = 0.5):
        self.p = probability  #probability score for adding nodes to new level
        self.head = ListNode(None)
        self.head_level_pointer = 1 # Length of Highest level pointer, added dynamically
        self.head.next = [None] #List of pointers pointing to next node for all the levels
        
        
    def lookup_search(self, target: int) -> bool:
        present = self.head
        if present == self.head and present.next[self.head_level_pointer-1] and present.next[self.head_level_pointer-1].val < target:
            present = present.next[self.head_level_pointer-1]
        #Searching for the target by traversing horizontally and vertically(downwards) along the levels
        l = self.head_level_pointer - 1
        while present.down != None or present == self.head:
            while present.next[l] and present.next[l].val < target:
                present = present.next[l]
            if present.next[l] and present.next[l].val == target:
                return True
            if l == 0:
                return False
            present = present.down
            l -= 1
        return False

    def insert(self, num: int) -> None:
        present = self.head
        temp = [None] * self.head_level_pointer #Intializtion to store previous nodes
        #Traversing throught nodes along the levels until we reach for the position to insert the element
        l = self.head_level_pointer - 1
        while l >= 0:
            while present.next[l] and num > present.next[l].val:
                present = present.next[l]
            temp[l] = present
            l -= 1
        #Calculating the number of levels that the new node appears throught probability distribution 
        new_num_levels = 1
        while random.random() > 0.5:
            new_num_levels += 1
        new_element = ListNode(num)
        new_element.next = [None] * new_num_levels
        
        #In case number of levels for new node exceeds the existing highest level than add head node to the temp for exceeding levels
        if new_num_levels > self.head_level_pointer:
            for l in range(self.head_level_pointer, new_num_levels):
                self.head.next.append(None)
                temp.append(self.head)
                if l > 0:
                    temp[l].down = self.head
            self.head_level_pointer = new_num_levels
        #Pointing the previous node pointers to the new node and the new node to itself through down pointer if number of levels is > 1
        l = 0
        while l < new_num_levels:
            new_element.next[l] = temp[l].next[l]
            temp[l].next[l] = new_element
            if l > 0:
                new_element.down = temp[l-1].next[l-1]
            l += 1

    def delete(self, num: int) -> bool:
        present = self.head
        temp = [None] * self.head_level_pointer #Intializtion to store previous nodes
        if present == self.head and present.next[self.head_level_pointer-1] and present.next[self.head_level_pointer-1].val < num:
            present = present.next[self.head_level_pointer-1]
        temp[self.head_level_pointer-1] = present
        #Searching for the target to be deleted by traversing horizontally and vertically(downwards) along the levels
        l = self.head_level_pointer - 1
        while present.down != None or present == self.head:
            while present.next[l] and present.next[l].val < num:
                present = present.next[l]
            temp [l] = present
            if present.next[l] and present.next[l].val == num:
                level = l
                delete_node = present.next[l]
                while level >= 0:
                    #Deleting the number by assigning previous node pointers to the next node
                    temp[l].next[level] = delete_node.next[level]
                    level -= 1
                return True
            if l == 0:
                return False
            present = present.down
            l -= 1
        return False