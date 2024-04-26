
#Problem 1

def get_distance(arr):
    size = len(arr)
    distance = 0
    
    if size == 0:
        return 0
    
    for i in range(8):
        setBits = 0
        for k in range(size):
            setBits = setBits + (arr[k] & 1)
            arr[k] = arr[k] >> 1
        distance += setBits * (size - setBits)   
    
    sum_of_pair_distances = 2 * distance

    return sum_of_pair_distances

#Problem 2

def move_steps(k):
    
    if k < 0:
        return 0
    if k == 0:
        return 1
    
    answer = move_steps(k - 1) + move_steps(k - 2)
    
    return answer

#Problem 3

def decode_message(s):
    s1 = s
    for i in range(len(s) + 1):
        if (i + 1) % 2 == 0 and i < len(s) - 1:
            if s[i] == s[i+1]:
                s = s[:i] + s[i+1:]
            else:
                return s1
    message = s
    return message

#Problem 4

def count_sub_strs(s: str):
    subStrings = []
    number_of_sub_strings = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            subStrings.append(s[i:j])
            
    for word in subStrings:
        if word[0] == 'a':
            noc = 0
            temp = 0
            for i in range(len(word)):
                if word[i] == 'a' and temp == 0:
                    noc += 1
                elif word[i] == 'b':
                    temp = 1
                    noc -= 1
                else:
                    temp = 0
                    break
            if noc == 0 and temp != 0:
                number_of_sub_strings += 1
        
        if word[0] == 'b':
            noc = 0
            temp = 0
            for i in range(len(word)):
                if word[i] == 'b' and temp == 0:
                    noc += 1
                elif word[i] == 'a':
                    temp = 1
                    noc -= 1
                else:
                    temp = 0
                    break
            if noc == 0 and temp != 0:
                number_of_sub_strings += 1  
                
          
    return number_of_sub_strings

#Problem 5
def check_transformation(s1, s2):
    used_char1 = []
    used_char2 = []
    if len(s1) != len(s2):
        return False
    for i in range(len(s1)):
        if s1[i] not in used_char1 and s2[i] not in used_char2:
            used_char1.append(s1[i])
            used_char2.append(s2[i])
            s1 = s1.replace(s1[i], s2[i])
            if s1 == s2:
                return True
    return False
