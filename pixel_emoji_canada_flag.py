from array import *

#red is 1, white is 0
canada_flag = [[1,1,1,0,0,0,0,0,0,0,1,1,1],
               [1,1,1,0,0,0,1,0,0,0,1,1,1],
               [1,1,1,0,1,0,1,0,1,0,1,1,1],
               [1,1,1,0,1,1,1,1,1,0,1,1,1],
               [1,1,1,0,0,1,1,1,0,0,1,1,1],
               [1,1,1,0,1,1,1,1,1,0,1,1,1],
               [1,1,1,0,0,0,1,0,0,0,1,1,1],
               [1,1,1,0,0,0,1,0,0,0,1,1,1],
               [1,1,1,0,0,0,0,0,0,0,1,1,1]]

print(".") # usually first line contains a username so print a . followed by a newline
for row in canada_flag:
    for col in row:
        if col == 1:
            print("🍁", end = '')
        else:
            print("🧊", end = '')
    print()

