import copy
import time

from ida_star import is_goal, get_successors

# in seconds
timeout = 60


# starts is the initial position of the tiles
# goals is the goal position of the tiles
# iterative depth first search
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

        # if the function finds the goal state
        if found is not None:
            # append start to the list
            found.append(starts)
            found.reverse()
            now = time.process_time() - start_time
            print('IDDFS took ' + str(now) + ' seconds to complete.')
            return found

        # if the path is not found at that depth
        elif not remaining:
            return None
        depth += 1


# curr is the current state of the tiles
# goal is the goal state of the tiles
# depth is the maximum depth of the search
# start_time is the maximum time the function can run until time out
def depth_limited_search(curr, goal, depth, start_time):

    # check if the run time has exceeded the time out time
    now = time.process_time() - start_time
    if now > timeout:
        return None, True

    # return if the goal state is reached at depth
    # return if it has not reached goal state but may have more children to consider
    if depth == 0:
        if is_goal(curr, goal):  # refer to ida_star for implementation
            return [curr], True
        else:
            return None, True
    else:
        any_remaining = False

        # find all children of curr
        successors = get_successors(curr)  # refer to ida_star for implementation
        for successor in successors:
            # for each successor, call search again with new arguments
            found, remaining = depth_limited_search(successor, goal, depth - 1, start_time)

            # if the function finds the goal state
            if found is not None:
                found.append(successor)
                return found, True

            # if the function has other children to consider
            elif remaining:
                any_remaining = True

        # if the function can not find a path
        return None, any_remaining
