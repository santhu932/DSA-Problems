# Problem 1

def longestPalindromeSubseq(s: str):
    str_len = len(s)

    #returns 0 if string in empty
    if str_len == 0:
        return 0
    
    #initializing matrix
    lps_matrix = [[0 for m in range(str_len)] for n in range(str_len)]

    #initializing diagonal of matrix with 1 for the substring of length 1
    for k in range(str_len):
        lps_matrix[k][k] = 1
  
    #calculating the entries of the matrix for substring of length greater than 1
    for sub_len in range(2, str_len + 1):
        for m in range(str_len - sub_len + 1):
            n = m + sub_len - 1
            if s[m] == s[n]:
                lps_matrix[m][n] = lps_matrix[m+1][n-1] + 2
            else:
                lps_matrix[m][n] = max(lps_matrix[m][n-1], lps_matrix[m+1][n])
    
    lps_length = lps_matrix[0][str_len - 1]
    
    return lps_length

#Problem 2

def CondensedIntegers(k, factors):
    if factors == []:
        return []
    
    #Creating the list to store multiples of the factors
    multiples_list = factors.copy()
    #Pointer list to store indices for all the factors in multiples list
    pointer_list = [0] * len(factors)
    
    #List to store condensed integers
    cond_ints = [0] * k
    cond_ints[0] = 1 # 1 is a condensed int for all prime factors
    
    #Calculating next k-1 condensed integers
    for c in range(1, k):
        min_int = min(multiples_list)
        min_index = multiples_list.index(min_int)
        cond_ints[c] = min_int
        pointer_list[min_index] += 1
        multiples_list[min_index] = cond_ints[pointer_list[min_index]] * factors[min_index]
        
        #Updating the other same minimum multiples in the list to avoid duplication
        while min_int == min(multiples_list):
            min_index = multiples_list.index(min_int)
            pointer_list[min_index] += 1
            multiples_list[min_index] = cond_ints[pointer_list[min_index]] * factors[min_index]
        
    return cond_ints

#Problem 3

def tower_rouge(tower):
    rows = len(tower)
    columns = len(tower[0])
    
    #Intializing the matrix for bottum up approach
    tower_matrix = [[0 for n in range(columns)] for m in range(rows)]
    

    for m in range(rows - 1, -1, -1):
        for n in range(columns - 1, -1, -1):
            #Calculating entry for tome room
            if m == rows - 1 and n == columns - 1:
                tower_matrix[m][n] = min(0, tower[m][n])
            #Calculating entry for last floor
            elif m == rows - 1:
                tower_matrix[m][n] = min(0, tower_matrix[m][n + 1] + tower[m][n])
            #Calculating entry for last rooms
            elif n == columns - 1:
                tower_matrix[m][n] = min(0, tower_matrix[m + 1][n] + tower[m][n])
            else:
                tower_matrix[m][n] = min(0, max(tower_matrix[m + 1][n], tower_matrix[m][n + 1]) + tower[m][n])
                
    minimum_starting_energy = abs(tower_matrix[0][0]) + 1
    return minimum_starting_energy

# Problem 4

def getMedian(arr1, arr2, n):
    
    #Returning -1 if they don't buy equal number of candies
    if len(arr1) != len(arr2):
        return -1
    
    return compute_median(arr1, 0, len(arr1) - 1, arr2, 0, len(arr2) - 1)

def compute_median(arr1, first1, last1, arr2, first2, last2):
    length = last1 - first1 + 1
    
    #Calculating the median when they both buy only one candy
    if length == 1:
        return (arr1[first1] + arr2[first2])/2
    #Calculating the median when they both buy only two candy
    if length == 2:
        return (max(arr1[first1], arr2[first2]) + min(arr1[last1], arr2[last2])) / 2
    
    #Calculating the median of arr1
    if length % 2 == 0:
        arr1_median = (arr1[length//2 + first1 - 1] + arr1[length//2 + first1]) / 2
    else:
        arr1_median = arr1[length//2 + first1]

    #Calculating the median of arr2
    if length % 2 == 0:
        arr2_median = (arr2[length//2 + first2 - 1] + arr2[length//2 + first2]) / 2
    else:
        arr2_median = arr2[length//2 + first2]
        
    #Returning the median if both are equal
    if arr1_median == arr2_median:
        return arr1_median
    
    #Dividing the arrays if the medians are not equal and computing the median recursively - Divide and Conqure approach
    if arr1_median >= arr2_median:
        if length % 2 == 0:
            return compute_median(arr1, first1, first1 + length//2, arr2, first2 + length//2 - 1, last2)
        else:
            return compute_median(arr1, first1, first1 + length//2, arr2, first2 + length//2, last2)
    else:
        if length % 2 == 0:
            return compute_median(arr1, first1 + length//2 - 1, last1, arr2, first2, first2 + length//2)
        else:
            return compute_median(arr1, first1 + length//2, last1, arr2, first2, first2 + length//2)
        
# Problem 5

def no_of_ways(n: int):
    #Return 0 if n is odd
    if n % 2 != 0:
        return 0
        
    #Intializing array to store number of ways
    count_arr = [0] * (n + 1)
    count_arr[0] = 1 #Base initialization
    count_arr[1] = 0 #odd n
    count_arr[2] = 3 #For n = 2

    #Computing the number of ways for n greater than 3
    for n1 in range(4, n+1, 2):
        count_arr[n1] = count_arr[n1-2] * 4 - count_arr[n1 - 4]
        
    return count_arr[n]
