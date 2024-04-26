#Problem 1

class amor_dict():
    def __init__(self, num_list = []):
        self.n = len(num_list)
        self.k = bin(self.n).replace("0b", "")
        self.am_dict = self.create_amor_dict(num_list)
        
    def create_amor_dict(self, num_list):
        curr_pointer = 0
        bin_rep = self.k
        a_dict = dict()
        for b in range(len(bin_rep)):
            if int(bin_rep[b]) == 1:
                i = len(bin_rep) - (b + 1)
                key = 2 ** i
                A_i = []
                for j in range(key):
                    A_i.append(num_list[curr_pointer + j])
                curr_pointer += key
                A_i.sort()
                a_dict[i] = A_i
        return a_dict

    def insert(self, num):
        updated_n = self.n + 1
        bin_rep = bin(updated_n).replace("0b", "")
        if len(bin_rep) > len(self.k):
            i = len(bin_rep) - 1
            temp_arr = [] + [num]
            keys = list(self.am_dict.keys())
            for key in keys:
                temp_arr += self.am_dict[key]
                del self.am_dict[key]
            temp_arr.sort()
            self.am_dict[i] = temp_arr
        else:
            keys = list(self.am_dict.keys())
            bin_rep_reverse = bin_rep[::-1]
            temp_arr = [] + [num]
            for i in range(len(bin_rep_reverse)):
                if i in keys:
                    temp_arr += self.am_dict[i]
                    del self.am_dict[i]
                else:
                    temp_arr.sort()
                    self.am_dict[i] = temp_arr
                    break
        self.n = updated_n
        self.k = bin_rep
     
    def binary_search(self, level_list, lower, upper, num):
        if upper >= lower:
            middle = (upper + lower) // 2
            
            if level_list[middle] == num:
                return middle
            elif level_list[middle] < num:
                return self.binary_search(level_list, middle + 1, upper, num)
            else:
                return self.binary_search(level_list, lower, middle -1 , num)
        else:
            return -1
        
    def search(self, num):
        keys = list(self.am_dict.keys())
        for i in keys:
            lower = 0
            upper = len(self.am_dict[i]) - 1
            if self.binary_search(self.am_dict[i], lower, upper, num) >= 0:
                return i
        return -1
    
    
    def print(self):
        dict_arr = []
        bin_rep = self.k
        for b in range(len(bin_rep)):
            i = len(bin_rep) - (b + 1)
            if i in self.am_dict.keys():
                dict_arr.append(self.am_dict[i])
            else:
                dict_arr.append([]) 
        dict_arr = dict_arr[::-1]
        return dict_arr
    
# Problem 2

def implement_queue(operations):
    s1 = []
    s2 = []
    output_list = []
    for s in operations:
        op = s.split('(')
        
        if op[0] == 'push':
            arg = op[1].split(')')[0]
            s1.append(int(arg))
            
        elif op[0] == 'peek':
            if s1 != []:
                while len(s1) > 0:
                    s2.append(s1.pop())
                output_list.append(s2[-1])
                while len(s2) > 0:
                    s1.append(s2.pop())
            else:
                output_list.append("#")
                    
        elif op[0] == 'pop':
            if s1 != []:
                while len(s1) > 0:
                    s2.append(s1.pop())
                output_list.append(s2.pop())
                while len(s2) > 0:
                    s1.append(s2.pop())
            else:
                output_list.append("#")
                    
        elif op[0] == 'empty':
            if s1 == []:
                output_list.append(True)
            else:
                output_list.append(False)
        
    return output_list