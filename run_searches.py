import argparse
import glob

from a_star import a_star
from ida_star import id_a_star
from id_dfs import id_depth_first
from read_instance import import_instance
from visualize import visualize_paths


# prints the instance
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

    for file in sorted(glob.glob(args.instance)):

        # import the instance
        print('**** IMPORT INSTANCE ****')
        starts, goals, blank_start, blank_goal = import_instance(file)
        print('Starting Locations:')
        print_instance(starts)
        print('Goal Locations:')
        print_instance(goals)

        # types of searches
        searches = ['A*', 'IDA*', 'IDDFS']  # ADD YOUR SEARCH HERE and in the for loop
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

            if search == 'IDDFS':
                path = id_depth_first(starts, goals)
                paths.append(path)
                if path is not None:
                    print('Finished IDDFS')

        # call visualizer
        if not args.batch:
            for x in range(len(searches)):
                if paths[x] is None:
                    continue
                visualize_paths(paths[x], searches[x])  # refer to visualize for implementation
