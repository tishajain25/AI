import os
--------------------------------------------------------------------------------------------------------
cwd = os.getcwd()
path_for_file = os.path.abspath('/Users/tishajain/Documents/Code/AI/input2.txt'). // and input.txt
--------------------------------------------------------------------------------------------------------
state_space = {}
--------------------------------------------------------------------------------------------------------
with open(path_for_file, 'r') as f:
    total_states = int(f.readline())
    
    for i in range(1, total_states + 1):
        l = f.readline().strip()
        if l == '':
            state_space[i] = []
            
        else:
            nbour = l.split(" ")
            nbour = [int(n) for n in nbour]
            state_space[i] = nbour
print(state_space)
-------------------------------------------------------------------------------------------------------
/*
text files for both input.txt and input2.txt

input.txt

8
1 2 4
1 2 5
3 4 7
3 4
5 6
5 6 8
7 8
7 8
1
7
----------------------------------------------------------------------------------------------------
input2.txt

7
2 3
4 5
6 7
5

7
4
1
6
*/
