import argparse
import glob
import concurrent.futures as futures
import sys

from a_star import a_star
from ida_star import id_a_star
from read_instance import import_instance
from visualize import visualize_paths
from divide_a_star import da_star
from new_divide_astar import dac_a_star

def print_instance(instance):
    for row in instance:
        for entry in row:
            print(entry.rjust(3), end='')
        print()


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Runs various MAPF algorithms')
    parser.add_argument('--instance', type=str, default=None,
                        help='The name of the instance file(s)')
    parser.add_argument('--batch', action='store_true', default=False,
                        help='Use batch output instead of animation')

    args = parser.parse_args()

    time_out = 30  # in seconds

    for file in sorted(glob.glob(args.instance)):

        print('**** IMPORT INSTANCE ****')
        starts, goals, blank_start, blank_goal = import_instance(file)
        print('Starting Locations:')
        print_instance(starts)
        print('Goal Locations:')
        print_instance(goals)

        #searches = ['A*', 'IDA*','DACA*']
        searches = ['DACA*']
        paths = []
        for search in searches:
            print('**** Starting ' + search + ' Search ****')

            if search == 'A*':
                path = a_star(starts, goals, blank_start)
                paths.append(path)
                if path is not None:
                    print('Finished A*')

            if search == 'IDA*':
                path = id_a_star(starts, goals)
                paths.append(path)
                if path is not None:
                    print('Finished IDA*')

            if search == 'DACA*':

                #path = da_star(starts, goals)
                path = dac_a_star(starts, goals)
                paths.append(path)

                if path is not None:
                    print('Finished IDA*')

        if not args.batch:
            for x in range(len(searches)):
                print("paths is")
                print(paths)
                if paths[x] is None:
                    continue
                visualize_paths(paths[x], searches[x])
