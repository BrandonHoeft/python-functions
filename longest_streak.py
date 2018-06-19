def longest_streak(var, value):

    current_streak = 0
    longest_streak = 0
    longest_streak_loc = 0

    for i in range(len(var)):
        if var[i] == value:
            current_streak += 1
            longest_streak = max(longest_streak, current_streak)
            print('if... ' + str(i) + ', ' + str(current_streak) + ', ' + str(longest_streak))

        else:
            longest_streak = max(longest_streak, current_streak)
            current_streak = 0
            print('else... ' + str(i) + ', ' + str(current_streak) + ', ' + str(longest_streak))

        if longest_streak == current_streak:
            longest_streak_loc = i

    print('longest streak of {}, ends at row index: {}'.format(longest_streak, longest_streak_loc)) 




# Testing #####################################################################
#          0 1 2 3 4 5 6 7 8 9
flips = [0,1,0,1,1,1,0,1,0,0] # length 10

#            0 1 2 3 4 5 6 7 8 9 1 1 2 3 4 5 6 7 8 9
flips20 = [0,1,0,1,1,1,0,1,0,0,1,1,1,1,0,0,0,1,1,1] # length 20

import numpy as np
np.random.seed(123)
flips1000 = [np.random.randint(0,2) for n in range(1000)]


print(longest_streak(flips, 1))
print(longest_streak(flips20, 1))
print(longest_streak(flips1000, 1))

for i, val in enumerate(flips1000):
    if i < 500:
        print(i, val, sep = ': ')

    