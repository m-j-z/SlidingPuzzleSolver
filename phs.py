import copy
import time

from a_star import move, swap, compute_heuristics, get_path
# in seconds
timeout = 60

def phs(starts, goals, blank_start):
    open_list = []
    closed_list = dict()
    root = {'loc': blank_start, 'h_val': compute_heuristics(starts, goals), 'timestep': 0,
            'positions': copy.deepcopy(starts), 'parent': None}
    open_list.append((0,root))


    start_time = time.process_time()
    expanded = 0
    generated = 0
    while len(open_list) > 0:
        open_list.sort(key=lambda x: x[0])
        _,curr = open_list.pop(0)
        closed_list[(curr['loc'], curr['timestep'])] = curr

        expanded += 1

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
            h_val = compute_heuristics(child['positions'], goals)
            if (child['loc'], child['timestep']) not in closed_list and  (h_val,child) not in open_list:
                if child['positions'] == goals:
                    print('PHS took ' + str(now) + ' seconds to complete.')
                    print('Generated', generated, 'nodes.')
                    print('Expanded', expanded, 'nodes.')
                    return get_path(child)
                else:
                    open_list.append((h_val,child))


    return None
