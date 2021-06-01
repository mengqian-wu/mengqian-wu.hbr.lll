import sys, operator, os, string, re
import itertools


# For Bates Story20 
alphebet_list = []
sign_list = []
f = open('200116_0021.txt', 'r')
for line in f:
    alphebet_list.append(line[0])
#print(alphebet_list)

for item in alphebet_list:
    if item == 'A':
        item = 1
    else:
        item = -1
    sign_list.append(item)
    
#print(sign_list)

# python code to find number of time sign changes in the lst
output = len(list(itertools.groupby(sign_list, lambda sign_list: sign_list >0)))
turn_taking = output - 1
print(turn_taking)

n = len(sign_list)
m = 0
c = 0
for element in sign_list:
    if element == 1:
        m += 1
    if element == -1:
        c += 1


print(n, m, c)

    
f.close()

# space smaller than the five seconds - one turn-taking
# B-C is not counted 
# don't count O as child utterance. 