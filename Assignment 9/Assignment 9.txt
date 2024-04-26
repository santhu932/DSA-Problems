#Problem 1

def get_finish_time(itr):
    return itr[1]

def maximum_intervals(intervals):
    # Arrange the intervals in order based on their finish times.
    intervals.sort(key=get_finish_time)
    # Initializing variables
    ct = 0
    finish_time = -float('inf')
    #Go through each interval and choose the ones that do not overlap with each other and have the earliest end times.
    for it in intervals:
        if finish_time <= it[0]:
            finish_time = it[1]
            ct += 1
    return ct

#Problem 2

def circular_tour(distance, charging):
    #Initialize the starting city
    s_city = 0
    # Initializing the gas tank variable
    tk = 0
    # Records the count of total gas shortage
    count = 0
    k = 0
    while k < len(distance):
        tk += charging[k] - distance[k]
        #update the starting city and the total gas shortage
        if tk < 0:
            count += tk
            s_city = k + 1
            tk = 0
        k += 1
   #Check completion a circular tour starting from the starting city
    if count + tk >= 0:
        return s_city
    else:
        return -1
        
        
#Did not get time to solve wavelet tree beacuse of other assignment deadlines
