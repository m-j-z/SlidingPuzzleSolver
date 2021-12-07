import sys
from a_star import a_star
from read_instance import import_instance
from id_a_star import id_a_star

if __name__ == '__main__':
    filename = sys.argv[1]
    starts, goals, blank_start, blank_goal = import_instance(filename)
    # paths = a_star(starts, goals, blank_start, blank_goal)
    # paths = iterative_deepening_a_star(starts, goals, blank_start, blank_goal)
    paths = id_a_star(starts, goals, blank_start, blank_goal)
    
    for x in paths:
        for p in x:
            print(p)
        print('')
    
    print('Number of steps:', len(paths) - 1)
        