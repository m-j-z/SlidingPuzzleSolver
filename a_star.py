import heapq
import copy
import time

# in seconds
timeout = 60


def move(loc, d):
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    return loc[0] + directions[d][0], loc[1] + directions[d][1]


# starts is a list of list
# curr is a tuple or list of 2 values
# child is a tuple or list of 2 values
# swaps the values inside starts from index of curr to index of child
def swap(starts, curr, child):
    tmp = starts[curr[0]][curr[1]]
    starts[curr[0]][curr[1]] = starts[child[0]][child[1]]
    starts[child[0]][child[1]] = tmp
    

# val is a value
# li is a list of lists
# gets the index of val from li
# i.e. will return (2, 1) if val is at row 2 column 1 in the list li
def get_index(li, val):
    for i, x in enumerate(li):
        if val in x:
            return i, x.index(val)
    

# computes heuristics for tile puzzles
# computes the distance from the values to the goal, except for 0 (the blank tile)
def compute_heuristics(current, goals):
    size = len(current) * len(current[0])
    
    h_value = 0
    for x in range(1, size):
        curr_index = get_index(current, str(x))
        goal_index = get_index(goals, str(x))
        h_value += (abs(goal_index[0] - curr_index[0])) + (abs(goal_index[1] - curr_index[1]))
        
    return h_value


def get_path(goal_node):
    path = []
    curr = goal_node
    while curr is not None:
        path.append(curr['positions'])
        curr = curr['parent']
    path.reverse()
    return path


def push_node(open_list, node):
    heapq.heappush(open_list, (node['g_val'] + node['h_val'], node['h_val'], node['loc'], node))


def pop_node(open_list):
    _, _, _, curr = heapq.heappop(open_list)
    return curr


def compare_nodes(n1, n2):
    """Return true is n1 is better than n2."""
    return n1['g_val'] + n1['h_val'] < n2['g_val'] + n2['h_val']


def a_star(starts, goals, blank_start):
    open_list = []
    closed_list = dict()
    root = {'loc': blank_start, 'g_val': 0, 'h_val': compute_heuristics(starts, goals), 'timestep': 0,
            'positions': copy.deepcopy(starts), 'parent': None}
    push_node(open_list, root)
    closed_list[(root['loc'], root['timestep'])] = root
    nodes_generated = 1
    nodes_expanded = 0



    start_time = time.process_time()
    while len(open_list) > 0:
        curr = pop_node(open_list)
        nodes_expanded += 1

        now = time.process_time() - start_time
        if now > timeout:
            print('Timed out!')
            return None

        if curr['positions'] == goals:
            print('A* took ' + str(now) + ' seconds to complete.')
            return (get_path(curr),nodes_expanded,nodes_generated)
        
        for d in range(4):
            child_loc = move(curr['loc'], d)
            if child_loc[0] < 0 or child_loc[0] > len(starts) - 1:
                continue
            if child_loc[1] < 0 or child_loc[1] > len(starts[0]) - 1:
                continue
            child = {'loc': child_loc,
                     'g_val': curr['g_val'] + 1,
                     'h_val': 0,
                     'timestep': curr['timestep'] + 1,
                     'positions': copy.deepcopy(curr['positions']),
                     'parent': curr}
            swap(child['positions'], curr['loc'], child['loc'])
            child['h_val'] = compute_heuristics(child['positions'], goals)
            if (child['loc'], child['timestep']) in closed_list:
                existing_node = closed_list[(child['loc'], child['timestep'])]
                if compare_nodes(child, existing_node):
                    closed_list[(child['loc'], child['timestep'])] = child
                    push_node(open_list, child)
                    nodes_generated +=1
            else:
                closed_list[(child['loc'], child['timestep'])] = child
                push_node(open_list, child)
                nodes_generated +=1
            
    return None
