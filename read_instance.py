import sys
from pathlib import Path


# filename is the file name
def import_instance(filename):
    f = Path(filename)
    if not f.is_file():
        raise BaseException(filename + ' does not exist.')
    f = open(filename, 'r')
    
    # read size of instance // r x c
    size = int(f.readline().replace('\n', ''))
    
    # initialize the lists
    start_locs = []
    goal_locs = []

    # read the starting locations
    for x in range(size):
        line = f.readline().replace('\n', '').split(' ')
        start_locs.append(line.copy())

    # read the goal locations
    for x in range(size):
        line = f.readline().replace('\n', '').split(' ')
        goal_locs.append(line.copy())
        
    # read start and goal locations of the blank tile
    line = f.readline().replace('\n', '').split(' ')
    start = (int(line[0]), int(line[1]))
    goal = (int(line[2]), int(line[3]))

    return [start_locs, goal_locs, start, goal]
            
if __name__ == '__main__':
    file = sys.argv[1]
    import_instance(file)
    