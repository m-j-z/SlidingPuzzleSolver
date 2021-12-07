import argparse
import glob
from a_star import a_star
from read_instance import import_instance
from ida_star import id_a_star


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Runs various MAPF algorithms')
    parser.add_argument('--instance', type=str, default=None,
                        help='The name of the instance file(s)')
    parser.add_argument('--batch', action='store_true', default=False,
                        help='Use batch output instead of animation')

    args = parser.parse_args()

    for file in sorted(glob.glob(args.instance)):

        print('**** IMPORT INSTANCE ****')
        starts, goals, blank_start, blank_goal = import_instance(file)

        searches = ['A*', 'IDA*']
        for search in searches:
            print('**** ' + search + ' ****')

            if search == 'A*':
                path = a_star(starts, goals, blank_start, blank_goal)

            if search == 'IDA*':
                path = id_a_star(starts, goals)
