import copy
import time

from a_star import compute_heuristics, get_index, swap

# in seconds
timeout = 60


# checks if the state of curr is the same as goals
def is_goal(curr, goals):
    return curr == goals


# curr is a list of lists
# finds the successors of a list
def get_successors(curr):
    # a list of all possible childresn of curr
    successors = []
    # get the index of the blank tile
    index = get_index(curr, '0')  # refer to a_star for implementation

    # create all possible children
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for move in moves:
        tmp = copy.deepcopy(curr)
        next_index = (index[0] + move[0], index[1] + move[1])

        # check if that the move is legal
        if next_index[0] < 0 or next_index[0] > len(curr) - 1 or next_index[1] < 0 or next_index[1] > len(curr[0]) - 1:
            continue

        # swap current to child location
        swap(tmp, index, next_index)  # refer to a_star for implementaiton
        successors.append(copy.deepcopy(tmp))
    return successors


def sort_successors(successors, goals, g):
    successors_f = []
    for successor in successors:
        f = g + compute_heuristics(successor, goals)
        successors_f.append(f)

    for i in range(1, len(successors_f)):
        key = successors_f[i]
        tmp = successors[i]
        j = i - 1
        while j >= 0 and key < successors_f[j]:
            successors_f[j + 1] = successors_f[j]
            successors[j + 1] = successors[j]
            j -= 1
        successors_f[j + 1] = key
        successors[j + 1] = tmp


# starts is the initial positions of the tiles
# goals is the final position of the tiles
def id_a_star(starts, goals):
    bound = compute_heuristics(starts, goals)
    path = [starts]

    start_time = time.process_time()
    generated_nodes = 0
    expanded_nodes = 0

    while True:

        t, generated, expanded = a_star(path, goals, 0, bound, start_time, generated_nodes, expanded_nodes)
        generated_nodes += generated
        expanded_nodes += expanded
        # if a path is found
        if t == -1:
            now = time.process_time() - start_time
            print('IDA* took ' + str(now) + ' seconds to complete.')
            print('Generated', generated_nodes, 'nodes.')
            print('Expanded', expanded_nodes, 'nodes.')
            return path
        # if there are no paths
        if t == float('inf'):
            return None
        # if it has timed out
        if t == float('-inf'):
            print('Timed out!')
            return None
        bound = t


# path is the path from starting positions to goal positions
# goals is the goal position
# g is the g value (a.k.a the distance traveled)
# bound is the maximum f value allowed for the search
# start_time is the maximum run time allowed until the function will time out
# recursive implementation of A* search
def a_star(path, goals, g, bound, start_time, generated, expanded):

    now = time.process_time() - start_time
    if now > timeout:
        return float('-inf'), generated, expanded
    
    node = path[-1]

    # computes the f value of the node
    f = g + compute_heuristics(node, goals)
    # checks if f value violates the bound
    if f > bound:
        return f, generated, expanded

    # return if node state is the goal state
    if is_goal(node, goals):
        return -1, generated, expanded

    m = float('inf')
    # get all successors of the node
    successors = get_successors(node)
    expanded += 1
    sort_successors(successors, goals, g)
    for successor in successors:
        if successor not in path:
            generated += 1
            path.append(copy.deepcopy(successor))
            # call with new arguments
            t, x, y = a_star(path, goals, g + 1, bound, start_time, generated, expanded)
            generated += x
            expanded += y

            # if it has timed out
            if t == float('-inf'):
                return float('-inf'), generated, expanded

            # if paths has been found
            if t == -1:
                return -1, generated, expanded

            # if path has not been found but there are still children nodes to check
            if t < m:
                m = t
            path.pop()
    return m, generated, expanded
    