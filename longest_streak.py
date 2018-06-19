def longest_streak(var, value):
    """Given a list, and a scalar value to be searched for in the list, return
    the maximum number of times this value occurs consecutively in the list."""
    
    current_streak = 0
    best_streak = 0
    best_streak_loc = 0

    for i in range(len(var)):
        if var[i] == value:
            current_streak += 1
            best_streak = max(best_streak, current_streak)

        else:
            best_streak = max(best_streak, current_streak)
            current_streak = 0
        
        # to ID the ending index where the best streak occurred. 
        if best_streak == current_streak: 
            best_streak_loc = i

    print('longest streak of {}, ends at row index: {}'.format(best_streak, best_streak_loc))
    
    return best_streak



# Testing #####################################################################
import numpy as np
np.random.seed(123)
flips1000 = [np.random.randint(0,2) for n in range(1000)]

print(longest_streak(flips1000, 1))

# inspect underlying data to validate results
for i, val in enumerate(flips1000):
    if i < 450:
        print(i, val, sep = ': ')
