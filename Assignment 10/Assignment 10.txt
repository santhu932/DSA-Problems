import heapq

#Problem 1

def removeStones(stones: list[list[int]]):
    g = {}
    seen = set()
     
    #Creating graph
    for m, (r1, c1) in enumerate(stones):
        for n, (r2, c2) in enumerate(stones):
            if r1 == r2 or c1 == c2:
                if m not in g:
                    g[m] = set()
                g[m].add(n)
                
    def dfs(loc):
        seen.add(loc)
        for adjacent in g[loc]:
            if adjacent not in seen:
                dfs(adjacent)
                
    # depth-first search to identify groups of nodes that are connected to each other
    ct = 0
    for s in range(len(stones)):
        if s not in seen:
            dfs(s)
            ct += 1
            
    count = len(stones) - ct

    return count

#Problem 2

def no_of_islands(map_grid):
    seen = set() #Keep track of visited loc
    if len(map_grid) == 0:
        return 0
    num_rows = len(map_grid)
    num_cols = len(map_grid[0])
    
    # Depth-First Search (DFS) to mark all the adjacent land cells that are connected to the given location.
    def dfs(m, n):
        if n < 0 or n >= num_cols or m < 0 or m >= num_rows:
            return
        if map_grid[m][n] == '0' or (m, n) in seen:
            return
        seen.add((m,n))
        dfs(m + 1, n)
        dfs(m - 1, n)
        dfs(m, n + 1)
        dfs(m, n - 1)
    ct = 0
    for k in range(num_rows):
        for l in range(num_cols):
            #If the cell is a land cell, increase the count and mark all adjacent connected land cells using dfs.
            if (k,l) not in seen and map_grid[k][l] == '1':
                dfs(k, l)
                ct = ct + 1
    return ct

#Problem 3

def cheapest_flight(n, tickets, start):
    # Set the distance of all nodes in a graph to Maximum distance, except for the start node.
    Max_dist = float('inf')
    d = [Max_dist] * n
    d[start] = 0
    
    # Make a priority queue and put the starting node in it.
    priority_q = [(0, start)]
    
    while len(priority_q) != 0:
        # Extract loc with smallest distance
        dist, city_x = heapq.heappop(priority_q)
        # check if the loc has already been explored.
        if dist > d[city_x]:
            continue
        
        for city_y in range(n):
            if tickets[city_x][city_y] != 0:
                new = d[city_x] + tickets[city_x][city_y]
            
                if new < d[city_y]:
                    heapq.heappush(priority_q, (new, city_y))
                    d[city_y] = new
            
    return d

# Problem 4

def number_of_moves(start_config, end_config, forbidden_config):
    f_config = set(forbidden_config)
    num_moves = {start_config: 0} #Create a dictionary that keeps track of the number of moves needed to reach each configuration.
    q = [start_config] #Create a queue to store configs that need to be checked
    
    while len(q) != 0:
        c = q.pop(0)
        
        #if the current configuration is equal to the end_config, return the corresponding number of moves.
        if c == end_config:
            return num_moves[c]
        
        for k in range(4):
            for l in [-1, 1]:
                #Create the subsequent configuration by modifying the current digit.
                next_c = c[:k] + str((int(c[k]) + l) % 10) + c[k+1:]
                
                if next_c not in f_config and next_c not in num_moves:
                    num_moves[next_c] = num_moves[c] + 1
                    q.append(next_c)
    
    return -1

# Problem 5

def word_games(word1, word2, dictionary):
    q = [(word1, 0)]
    seen = set([word1]) #Set to store visited words
    while len(q) != 0:
        #Retrive the next word and number of operations from the queue
        w, no_ops = q.pop(0)
        #If we have reached the target word2, return the number of operations
        if w == word2:
            return no_ops
        
        for k in range(len(w)):
            #Replace each letter with all 26 characters in the alphabet and check if the resulting word is in the dictionary.
            for ch in "abcdefghijklmnopqrstuvwxyz":
                
                if ch != w[k]:
                    w_new = w[:k] + ch + w[k+1:]
                    #Check if the new word is in the dictionary and has not been seen yet
                    if w_new in dictionary and w_new not in seen:
                        seen.add(w_new)
                        q.append((w_new, no_ops+1))
    return -1

