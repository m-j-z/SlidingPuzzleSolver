import copy
import time
from a_star import compute_heuristics, get_index, swap

# in seconds
timeout = 2


def id_a_star(starts, goals):
    
    bound = compute_heuristics(starts, goals)
    path = [starts]

    start_time = time.process_time()

    while True:

        t = a_star(path, goals, 0, bound, start_time)
        if t == -1:
            now = time.process_time() - start_time
            print('IDA* took ' + str(now) + ' seconds to complete.')
            return path
        if t == float('inf'):
            return None
        if t == float('-inf'):
            print('Timed out!')
            return None
        bound = t
    
    return None


def is_goal(curr, goals):
    return curr == goals


def get_successors(curr):
    successors = []
    index = get_index(curr, '0')
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for move in moves:
        tmp = copy.deepcopy(curr)
        next_index = (index[0] + move[0], index[1] + move[1])
        if next_index[0] < 0 or next_index[0] > len(curr) - 1 or next_index[1] < 0 or next_index[1] > len(curr[0]) - 1:
            continue
        swap(tmp, index, next_index)
        successors.append(copy.deepcopy(tmp))
    return successors


def a_star(path, goals, g, bound, start_time):

    now = time.process_time() - start_time
    if now > timeout:
        return float('-inf')
    
    node = path[-1]
    f = g + compute_heuristics(node, goals)
    if f > bound:
        return f
    if is_goal(node, goals):
        return -1
    m = float('inf')
    successors = get_successors(node)
    for successor in successors:
        if successor not in path:
            path.append(copy.deepcopy(successor))
            t = a_star(path, goals, g + 1, bound, start_time)
            if t == float('-inf'):
                return float('-inf')
            if t == -1:
                return -1
            if t < m:
                m = t
            path.pop()
    return m
    