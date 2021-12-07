import copy
from a_star import compute_heuristics, get_index, swap


def id_a_star(starts, goals, blank_start, blank_goal):
    
    bound = compute_heuristics(starts, goals)
    path = [starts]
    
    while True:
        t = a_star(path, goals, 0, bound)
        if t < 0:
            return path
        if t == float('inf'):
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


def a_star(path, goals, g, bound):
    
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
            t = a_star(path, goals, g + 1, bound)
            if t < 0:
                return -1
            if t < m:
                m = t
            path.pop()
    return m
    