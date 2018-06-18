
actions = [0,1,0,1,1,1,0,1,0,0]

def longest_streak(var):

    streak = 1
    best_streak = 1
    best_streak_i = 0

    for i in range(len(var)-1):
        print(str(i) + ' iteration') # testing/scaffolding
        if var[i] == var[i + 1] and streak >= best_streak:
            streak += 1
            best_streak = streak
            best_streak_i = i
        else:
            streak = 1 # reset streak
        print(str(streak))

    print('longest streak of {}, starts at index: {}'.format(best_streak, best_streak_i)) # testing/scaffolding
