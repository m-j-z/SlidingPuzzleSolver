import copy
import time
from a_star import swap

# in seconds
timeout = 4500


def dac_a_star(starts, goals):
    exist = []
    for g in range(len(goals) * len(goals[0])):
        exist.append(str(g))
    bound = compute_heuristics(starts, goals,exist)
    oldb = bound
    path = [starts]

    start_time = time.process_time()
    #setup
    height = len(goals)
    width = len(goals[0])
    # rebuilding
    losttop = []
    lostleft = []

    iter_height = 0
    iter_width = 0

    path_list = []
    generated_nodes = 0
    expanded_nodes = 0

    while True:

        if height == width: #Even chop off top

            fake_goal = goals.copy()
            placeholder = []
            for y in range(width):
                placeholder.append('x')
            for i in range(height):
                if i > 0:
                    fake_goal[i] = placeholder.copy()
            t, generated, expanded = a_star(path, fake_goal, 0, bound, start_time, goals,exist, generated_nodes, expanded_nodes)
            generated_nodes += generated
            expanded_nodes += expanded

            if t == -1:

                height -= 1
                pathlen = len(path)
                started = copy.deepcopy(path[pathlen - 1])

                #rebuild
                s_iter_height = iter_height
                s_iter_width = iter_width

                while s_iter_height != 0 or s_iter_width != 0:

                    if s_iter_width != 0:
                        to_linsert = lostleft[len(lostleft) - s_iter_width]
                        to_l_rebuild = []
                        for l in to_linsert:
                            to_l_rebuild.append(l[0])

                        widd = len(path[0])
                        for i in range(len(path)):

                            for w in range(widd):
                                path[i][w].insert(0, to_l_rebuild[w])
                        s_iter_width -= 1
                    if s_iter_height != 0:

                        to_tinsert = losttop[s_iter_height-1]
                        for tomod in path:
                            tomod.insert(0,to_tinsert.copy())
                        s_iter_height -= 1

                path_list.append((path.copy()))
                losttop.insert(0, copy.deepcopy(started[0]))
                path = copy.deepcopy(started)
                remove = path.pop(0)
                goals.pop(0)
                for w in remove:
                    if str(w) in exist:
                        exist.remove(w)

                path = [path]
                iter_height += 1
                t = oldb





        elif width==3 and height==2:#3x2 final
            fake_goal = goals.copy()
            placeholder = []

            #t = a_star(path, fake_goal, 0, bound, start_time, goals,exist)
            t, generated, expanded = a_star(path, fake_goal, 0, bound, start_time, goals, exist, generated_nodes,
                                            expanded_nodes)
            generated_nodes += generated
            expanded_nodes += expanded
            if t == -1:

                s_iter_height = iter_height
                s_iter_width = iter_width


                while s_iter_height > 0 or s_iter_width > 0:

                    if s_iter_height != 0:
                        to_tinsert = losttop.pop(0)
                        for tomod in path:
                            tomod.insert(0, to_tinsert.copy())
                        s_iter_height -= 1


                    if s_iter_width != 0:

                        to_linsert = lostleft.pop(0)
                        to_l_rebuild = []
                        for l in to_linsert:
                            to_l_rebuild.append(l[0])
                        widd = len(path[0])
                        for i in range(len(path)):
                            for w in range(widd):
                                path[i][w].insert(0, to_l_rebuild[w])
                        s_iter_width -= 1

                #adding to end
                for w in reversed(path_list):
                    for y in reversed(w):
                        to_finalize = y.copy()
                        path.insert(0, to_finalize)


        elif width - height == 1:# Odd shape

            fake_goal = []
            placeholder = []
            for y in range(width):
                placeholder.append('x')
            for k in range(height):
                fake_goal.append(placeholder.copy())
            for x in range(height):
                fake_goal[x][0] = goals[x][0]
            t, generated, expanded = a_star(path, fake_goal, 0, bound, start_time, goals, exist, generated_nodes,
                                            expanded_nodes)
            generated_nodes += generated
            expanded_nodes += expanded

            if t == -1:

                width -= 1
                pathlen = len(path)
                started = copy.deepcopy(path[pathlen - 1])
                saved_path = copy.deepcopy(path)

                s_iter_height = iter_height
                s_iter_width = iter_width

                while s_iter_height != 0 or s_iter_width != 0:
                    if s_iter_height != 0:
                        to_tinsert = losttop[s_iter_height-1]
                        for tomod in path:
                            tomod.insert(0,to_tinsert.copy())
                        s_iter_height -= 1
                    if s_iter_width != 0:
                        to_linsert = lostleft[len(lostleft) - s_iter_width]
                        to_l_rebuild = []
                        for l in to_linsert:
                            to_l_rebuild.append(l[0])
                        widd = len(path[0])

                        for y in range(len(saved_path)):
                            for z in range(widd):
                                path[y][z].insert(0,to_l_rebuild[z])
                        s_iter_width -= 1

                path_list.append(path.copy())
                path = started.copy()
                lostleft.insert(0, copy.deepcopy(started))
                #create new path for later
                for p in range(width):
                     remove = path[p].pop(0)
                     if remove in exist:
                        exist.remove(remove)


                     goals[p].pop(0)

                path = [path]

                iter_width += 1
                t = oldb


        if t == -1:
            now = time.process_time() - start_time
            print('DACA* took ' + str(now) + ' seconds to complete.')
            print('Generated', generated_nodes, 'nodes.')
            print('Expanded', expanded_nodes, 'nodes.')
            return path
        if t == float('inf'):
            return None
        if t == float('-inf'):
            print('Timed out!')
            print(path)
            return None
        bound = t

    return None


def get_index(li, val):
    for i, x in enumerate(li):
        if val in x:
            return (i, x.index(val))


def compute_heuristics(current, goals,exist):
    size = len(current) * len(current[0])

    h_value = 0

    for x in range(1, size):
        if str(x) in exist:

            curr_index = get_index(current, str(x))
            goal_index = get_index(goals, str(x))


            h_value += (abs(goal_index[0] - curr_index[0])) + (abs(goal_index[1] - curr_index[1]))

    return h_value

def n_compute_heuristics(current, goals,corrected):
    size = len(current) * len(current[0])
    h_value = 0

    for x in range(1, size):
        down = int(x / len(current[0]))
        left = int(x % len(current[0]))

        if not (current[down][left]) == 'x':
            strc = current[down][left]
            cont = False
            for u in goals:
                for o in u:
                    if strc == o:
                        cont = True
            if cont:
                curr_index = get_index(current, strc)
                goal_index = get_index(goals, strc)
                h_value += (abs(goal_index[0] - curr_index[0])) + (abs(goal_index[1] - curr_index[1]))

    return h_value


def is_goal(curr, goals):
    checker = copy.deepcopy(curr)
    size = len(checker) * len(checker[0])
    for x in range(1, size):
        down = int(x / len(checker[0]))
        left = int(x % len(checker[0]))
        if (goals[down][left]) == 'x':
            checker[down][left] = 'x'

    return checker == goals

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


def a_star(path, goals, g, bound, start_time,true_goal,exist,generated,expanded):
    now = time.process_time() - start_time
    if now > timeout:
        return float('-inf'), generated, expanded

    node = path[-1]

    f = g + compute_heuristics(node, true_goal,exist)
    if f > bound:
        return f, generated, expanded
    if is_goal(node, goals):
        return -1, generated, expanded
    m = float('inf')
    successors = get_successors(node)
    expanded += 1
    for successor in successors:
        if successor not in path:
            generated += 1
            path.append(copy.deepcopy(successor))
            t, x, y = a_star(path, goals, g + 1, bound, start_time,true_goal,exist,generated,expanded)
            if t == float('-inf'):
                return float('-inf'), generated, expanded
            if t == -1:
                return -1, generated, expanded
            if t < m:
                m = t
            path.pop()
    return m, generated, expanded
