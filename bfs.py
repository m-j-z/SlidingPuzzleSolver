import copy
import time

from a_star import move, swap, get_path
# in seconds
timeout = 60

def bfs(starts, goals, blank_start):
    open_list = []
    closed_list = dict()
    root = {'loc': blank_start, 'timestep': 0,
            'positions': copy.deepcopy(starts), 'parent': None}
    open_list.append(root)


    start_time = time.process_time()
    expanded = 0
    generated = 0
    while len(open_list) > 0:
        curr = open_list.pop(0)
        closed_list[(curr['loc'], curr['timestep'])] = curr

        expanded += 1


        if curr['positions'] == goals:
            print('bfs took ' + str(now) + ' seconds to complete.')
            print('Generated', generated, 'nodes.')
            print('Expanded', expanded, 'nodes.')
            return get_path(child)



        now = time.process_time() - start_time
        if now > timeout:
            print('Timed out!')
            return None

            

        print("expanded nodes: " + str(expanded))
        
        for d in range(4):
            child_loc = move(curr['loc'], d)
            if child_loc[0] < 0 or child_loc[0] > len(starts) - 1:
                continue
            if child_loc[1] < 0 or child_loc[1] > len(starts[0]) - 1:
                continue
            child = {'loc': child_loc,
                     'timestep': curr['timestep'] + 1,
                     'positions': copy.deepcopy(curr['positions']),
                     'parent': curr}
            generated += 1
            swap(child['positions'], curr['loc'], child['loc'])
            if (child['loc'], child['timestep']) in closed_list:
                continue   
            if (child) in open_list:
                continue
            open_list.append(child)


    return None
