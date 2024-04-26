# Problem 1

def subset_sum(nums: list[int], sum: int):
    
    #Returning True if list or sum is empty
    if sum == 0 or len(nums) == 0:
        return True
    
    set_size = len(nums)
    check_table = [[False for m in range(sum+1)] for n in range(set_size + 1)]
    
    #Base Initialization
    for m in range(len(nums)):
        check_table[m][0] = True
        
    col = 1
    while col <= sum:
        check_table[0][col] = False
        col += 1
        
    for m in range(1, set_size + 1):
        for n in range(1, sum + 1):
            if nums[m-1] > n :
                check_table[m][n] = check_table[m-1][n]
            else:
                check_table[m][n] = check_table[m-1][n-nums[m-1]] or check_table[m-1][n]
                
    return check_table[set_size][sum]

# Problem 2

def min_trials(n, k):
    trail_matrix = [[0 for r in range(k + 1)] for c in range(n + 1)]
    
    #Base Initialization
    for k1 in range(k + 1):
        trail_matrix[1][k1] = k1

    for r in range(2, n+1):
        for c in range(1, k+1):
            if r > c:
                trail_matrix[r][c] = trail_matrix[r-1][c]
            else:
                #Storing the maximum possible value and iterating over all the floors
                trail_matrix[r][c] = 999999
                for floor in range(1, k+1):
                    trails = 1 + max(trail_matrix[r-1][floor-1], trail_matrix[r][c-floor])
                    if trails < trail_matrix[r][c]:
                        trail_matrix[r][c] = trails
                        
    return trail_matrix[n][k]

# Problem 3

def split_rope(prices, n):
    
    #Table intialization
    prize_table = [[0 for col in range(n + 1)] for row in range(n + 1)]
    
    for m in range(1, n + 1):
        for n in range(1, n + 1):
            #Initializing when only prize for rope of length 1 is available
            if m == 1:
                prize_table[m][n] = prices[m-1] * n
            else:
                if n >= m:
                    prize_table[m][n] = max(prize_table[m-1][n], prize_table[m][n-m] + prices[m-1])
                else:
                    prize_table[m][n] = prize_table[m-1][n]
                    
                    
    best = prize_table[len(prices)][n]
    return best

# Problem 4

def sumCount(m,n,x):
    
    ways_table = [[0 for col in range(x + 1)] for row in range(n + 1)]
    
    ways_table[0][0] = 1
    
    for d in range(1, n + 1):
        for s in range(1, x + 1):
            #Iterating over all possible face values
            face = 1
            while face <= m:
                #Checking for the negative that is when sum exceeds scenario
                if s >= face:
                    ways_table[d][s] +=  ways_table[d-1][s-face]
                face += 1
    
    number_of_ways = ways_table[n][x]
    return number_of_ways

# Problem 5

def num_combinations(code, M):
    
    modulo = 10**9 + 7
    comb_table = [0] * (len(code) + 1)
    comb_table[0] = 1 #Base Condition
    
    for l in range(1, len(code) + 1):
        f = l - 1
        while f >= 0:
            #Checking if the integer is in 1 - M
            if M < int(code[f:l]):
                break 

            #Skipping trailing zeros
            elif code[f] == '0':
                f -= 1
                continue
            else:
                comb_table[l] = comb_table[l] + comb_table[f]
                comb_table[l] = comb_table[l] % modulo
            f -= 1
            
    num_of_comb_possible = comb_table[len(code)]
    return num_of_comb_possible


