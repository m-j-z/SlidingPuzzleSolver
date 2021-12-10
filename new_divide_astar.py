import copy
import time
from a_star import swap

# in seconds
timeout = 180


def dac_a_star(starts, goals):
    exist = []
    for g in range(len(goals) * len(goals[0])):
        exist.append(str(g))
    bound = compute_heuristics(starts, goals,exist)
    oldb = bound
    path = [starts]



    start_time = time.process_time()
    #setup
    path_holder = [get_index(starts, '0')]
    print("height and width is:")
    print(len(goals), len(goals[0]))
    height = len(goals)
    width = len(goals[0])
    # rebuilding
    losttop = []
    lostleft = []
    o_height = height
    o_width = width

    iter_height = 0
    iter_width = 0

    placeholder = []  # form x
    first_goal = goals.copy()
    fake_goal = goals.copy()
    fin = False
    path_list = []

    while True:

        if height == width: #Even chop off top
            #t = a_star(path, fake_goal, 0, bound, start_time, goals)
            print("Here")
            print(path)
            print(goals)
            print(height)
            print(width)
            fake_goal = goals.copy()
            placeholder = []
            for y in range(width):
                placeholder.append('x')
            print(fake_goal)
            for i in range(height):
                if i > 0:
                    fake_goal[i] = placeholder.copy()
            print("Fake Goal is")

            print(fake_goal)
            print("path is")
            print(path)
            print(exist)
            t = a_star(path, fake_goal, 0, bound, start_time, goals,exist)


            if t == -1:

                height -= 1
                pathlen = len(path)
                started = copy.deepcopy(path[pathlen - 1])
                print("ended starting to add losttop")
                print(started[0])

                print(losttop)
                print("fin lost top")
                print("new node is ")
                print("path is ")

                saved_path = copy.deepcopy(path)
                print(saved_path)
                #rebuild
                s_iter_height = iter_height
                s_iter_width = iter_width

                while s_iter_height != 0 or s_iter_width != 0:
                    top_shaved = False
                    if s_iter_width != 0:
                        print("even shape left shave")
                        to_linsert = lostleft[len(lostleft) - s_iter_width]
                        to_l_rebuild = []
                        for l in to_linsert:
                            to_l_rebuild.append(l[0])
                        print("rebuild")
                        print(to_l_rebuild)
                        print(len(path))
                        widd = len(path[0])
                        for i in range(len(path)):
                            #print(path[i])
                            #print(path[i][0])
                            for w in range(widd):
                                path[i][w].insert(0, to_l_rebuild[w])
                        s_iter_width -= 1
                    print("After math left shave is ")
                    if s_iter_height != 0:
                        print("even shape top shave")
                        to_tinsert = losttop[s_iter_height-1]
                        for tomod in path:
                            tomod.insert(0,to_tinsert.copy())
                        s_iter_height -= 1
                        top_shaved = True
                    print("After math top shave is ")
                    print(path)


                print("saved path is ")
                print(saved_path)

                path_list.append((path.copy()))
                losttop.insert(0, copy.deepcopy(started[0]))
                path = copy.deepcopy(started)

                print("top path is ")
                print(path)
                #new new path
                print("to remove top is")
                remove = path.pop(0)
                print(remove)
                goals.pop(0)
                for w in remove:
                    if str(w) in exist:
                        exist.remove(w)
                print("exist is now")
                print(exist)

                path = [path]
                print("final")

                #path = saved_path
                print(path)

                print(goals)
                print(losttop)

                iter_height += 1
                t = oldb





        elif width==3 and height==2:#3x2 final
            print("Here finally")
            print(path)
            print(goals)
            print(height)
            print(width)
            fake_goal = goals.copy()
            placeholder = []
            print(fake_goal)
            print("Fake Goal is")

            print(fake_goal)
            print("path is")
            print(path)
            print(exist)



            t = a_star(path, fake_goal, 0, bound, start_time, goals,exist)
            if t == -1:
                print("Finalizing")
                print("lost top")
                print(losttop)
                print(lostleft)
                print("Iters are ")
                print(iter_height)
                print(iter_width)

                s_iter_height = iter_height
                s_iter_width = iter_width

                while s_iter_height > 0 or s_iter_width > 0:
                    top_shaved = False
                    if s_iter_height != 0:
                        print("even shape top shave")
                        to_tinsert = losttop.pop(0)
                        for tomod in path:
                            tomod.insert(0, to_tinsert.copy())
                        s_iter_height -= 1
                        top_shaved = True
                    print("After math top shave is ")
                    print(path)
                    if s_iter_width != 0:
                        print("even shape left shave")
                        to_linsert = lostleft.pop(0)
                        to_l_rebuild = []
                        for l in to_linsert:
                            to_l_rebuild.append(l[0])
                        print("rebuild")
                        print(to_l_rebuild)
                        print(len(path))
                        widd = len(path[0])
                        for i in range(len(path)):
                            # print(path[i])
                            # print(path[i][0])
                            for w in range(widd):
                                path[i][w].insert(0, to_l_rebuild[w])
                        s_iter_width -= 1

                    print("After math left shave is ")
                    print(path)
                    print("Iter is not")
                    print(iter_height)
                    print(iter_width)



                    # for i in path:
                    #     to_pop = to_linsert.pop(0).copy()
                    #     for s in i:
                    #         s.insert




                #path[0][0].insert(0,'1')
                #
                #path[0][1].insert(0,'5')
                print("mod path is ")
                print(path)


        elif width - height == 1:# Odd shape
            print("Goals is")
            print(goals)
            print("Path")

            fake_goal = []
            placeholder = []
            for y in range(width):
                placeholder.append('x')
            for k in range(height):
                fake_goal.append(placeholder.copy())
            print(fake_goal)
            for x in range(height):
                print("x is ")
                print(x)
                print(goals[x][0])
                fake_goal[x][0] = goals[x][0]
            print("Fake Goal is")
            print(fake_goal)
            #fake_goal = [['1', 'x', 'x', 'x'], ['5', 'x', 'x', 'x'], ['9', 'x', 'x', 'x']]
            t = a_star(path, fake_goal, 0, bound, start_time,goals,exist)


            if t == -1:

                width -= 1
                pathlen = len(path)
                started = copy.deepcopy(path[pathlen - 1])
                print("started is")
                print(started)

                print("fin lost left")
                print("new node is ")
                saved_path = copy.deepcopy(path)

                #rebuild
                # s_iter_height = iter_height
                # if s_iter_height != 0:
                #     to_linsert = lostleft[len(lostleft) - iter_width]
                #     to_l_rebuild = []
                #     for l in to_linsert:
                #         to_l_rebuild.append(l[0])
                #     print("rebuild")
                #     print(to_l_rebuild)
                #     print(len(saved_path))
                #     widd = len(saved_path[0])
                #     for i in range(len(saved_path)):
                #         # print(path[i])
                #         # print(path[i][0])
                #         for w in range(widd):
                #             saved_path[i][w].insert(0, to_l_rebuild[w])
                s_iter_height = iter_height
                s_iter_width = iter_width
                # while s_iter_height is not 0:
                #     print("even shape top shave")
                #     to_tinsert = losttop[s_iter_height-1]
                #     for tomod in saved_path:
                #         tomod.insert(0,to_tinsert.copy())
                #     s_iter_height -= 1
                # s_iter_width = iter_width
                # while s_iter_width is not 0:
                #     print("even shape left shave")
                #     to_linsert = lostleft[len(lostleft) - s_iter_width]
                #     to_l_rebuild = []
                #     for l in to_linsert:
                #         to_l_rebuild.append(l[0])
                #     print("rebuild")
                #     print(to_l_rebuild)
                #     print(len(saved_path))
                #     widd = len(saved_path[0])
                #     for i in range(len(saved_path)):
                #         #print(path[i])
                #         #print(path[i][0])
                #         for w in range(widd):
                #             saved_path[i][w].insert(0,to_l_rebuild[w])
                #     s_iter_width -= 1

                while s_iter_height != 0 or s_iter_width != 0:
                    if s_iter_width != 0:
                        print("even shape left shave")
                        to_linsert = lostleft[len(lostleft) - s_iter_width]
                        to_l_rebuild = []
                        for l in to_linsert:
                            to_l_rebuild.append(l[0])
                        print("rebuild")
                        print(to_l_rebuild)
                        print(len(saved_path))
                        widd = len(saved_path[0])
                        for i in range(len(saved_path)):
                            #print(path[i])
                            #print(path[i][0])
                            for w in range(widd):
                                path[i][w].insert(0,to_l_rebuild[w])
                        s_iter_width -= 1
                    print("After math left shave is ")
                    if s_iter_height != 0:
                        print("even shape top shave")
                        to_tinsert = losttop[s_iter_height-1]
                        for tomod in path:
                            tomod.insert(0,to_tinsert.copy())
                        s_iter_height -= 1
                    print("After math top shave is ")
                    print(path)

                    print(path)


                #test
                # for w in reversed(path_list):
                #     for y in reversed(w):
                #         print("ptinign y")
                #         print(y)
                #         to_finalize = y.copy()
                #         saved_path.insert(0, to_finalize)
                print("to remove is")
                remove = []
                for mini in path:
                    remove.append(mini[0].copy())
                print(remove)
                #goals.pop(0)
                for w in remove:
                    if str(w) in exist:
                        exist.remove(w)
                print("exist is now")
                print(exist)

                #f_test_path = copy.deepcopy(saved_path)
                print("left path is")
                print(path)
                print("saved path is ")
                print(saved_path)




                path_list.append(path.copy())
                path = started.copy()
                lostleft.insert(0, copy.deepcopy(started))
                print("old path is ")
                print(path)
                #create new path for later
                for p in range(width):

                     remove = path[p].pop(0)
                     exist.remove(remove)
                     print(path[p][0])

                     goals[p].pop(0)


                path = [path]



                print("final ll")
                print(path)
                print(goals)

                print(lostleft)
                #path = f_test_path

                iter_width += 1
                t = oldb


        if t == -1:
            now = time.process_time() - start_time
            print('DACA* took ' + str(now) + ' seconds to complete.')
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


    #print("Down and left are")
    #print(down, left)
    #print(current[down][left])
    #
    for x in range(1, size):
        if str(x) in exist:

            down = int(x / len(current[0]))
            left = int(x % len(current[0]))
            #print("x is ")
            #print(x)
            #print(current)
            #print(goals)


            curr_index = get_index(current, str(x))
            goal_index = get_index(goals, str(x))
            print("g and c index are ")
            print(goal_index)
            print(curr_index)

            #print("here")
            h_value += (abs(goal_index[0] - curr_index[0])) + (abs(goal_index[1] - curr_index[1]))

            print(h_value)

    print(h_value)

    return h_value
def n_compute_heuristics(current, goals,corrected):
    size = len(current) * len(current[0])
    h_value = 0

    for x in range(1, size):
        down = int(x / len(current[0]))
        left = int(x % len(current[0]))
        print("Down and left are")
        print(down, left)
        print(current[down][left])


        if not (current[down][left]) == 'x':
            strc = current[down][left]
            #print("strc is")
            #print(strc)
            cont = False
            for u in goals:
                for o in u:
                    if strc == o:
                        cont = True
            if cont:
                curr_index = get_index(current, strc)
                goal_index = get_index(goals, strc)
                #print("c+g")
                #print(curr_index)
                #print(goal_index)
                h_value += (abs(goal_index[0] - curr_index[0])) + (abs(goal_index[1] - curr_index[1]))
                print("cur hval")
                print(h_value)

    return h_value


def is_goal(curr, goals):
    checker = copy.deepcopy(curr)
    print("Checking Goal")
    print(goals)
    size = len(checker) * len(checker[0])
    print("size is")
    print(size)
    for x in range(1, size):
        down = int(x / len(checker[0]))
        left = int(x % len(checker[0]))
        #print("G Down and left are")
        #print(down, left)
        if (goals[down][left]) == 'x':
            #print("found x")
            checker[down][left] = 'x'
    print("To compare to goal is")
    print(checker)
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


def a_star(path, goals, g, bound, start_time,true_goal,exist):
    now = time.process_time() - start_time
    if now > timeout:
        return float('-inf')

    node = path[-1]

    print("Start  of new A*")
    print("node is")
    print(node)
    print("goal is")
    print(goals)


    f = g + compute_heuristics(node, true_goal,exist)
    if f > bound:
        return f
    if is_goal(node, goals):
        return -1
    m = float('inf')
    successors = get_successors(node)
    for successor in successors:
        if successor not in path:
            path.append(copy.deepcopy(successor))
            t = a_star(path, goals, g + 1, bound, start_time,true_goal,exist)
            if t == float('-inf'):
                return float('-inf')
            if t == -1:
                return -1
            if t < m:
                m = t
            path.pop()
    return m