import copy
import time

from ida_star import is_goal, get_successors

# in seconds
timeout = 2


def id_depth_first(starts, goals):
    root = copy.deepcopy(starts)
    depth = 0
    start_time = time.process_time()
    while True:
        now = time.process_time() - start_time
        if now > timeout:
            print('Timed out!')
            return None
        found, remaining = depth_limited_search(root, goals, depth, start_time)
        if found is not None:
            found.append(starts)
            found.reverse()
            return found
        elif not remaining:
            return None
        depth += 1


def depth_limited_search(curr, goal, depth, start_time):

    now = time.process_time() - start_time
    if now > timeout:
        return None, True

    if depth == 0:
        if is_goal(curr, goal):
            return [curr], True
        else:
            return None, True
    else:
        any_remaining = False
        successors = get_successors(curr)
        for successor in successors:
            found, remaining = depth_limited_search(successor, goal, depth - 1, start_time)
            if found is not None:
                found.append(successor)
                return found, True
            elif remaining:
                any_remaining = True
        return None, any_remaining
