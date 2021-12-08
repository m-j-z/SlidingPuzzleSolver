import argparse
import glob
import concurrent.futures as futures
import sys

from a_star import a_star
from ida_star import id_a_star
from read_instance import import_instance
from visualize import visualize_paths


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

    time_out = 2  # in seconds

    for file in sorted(glob.glob(args.instance)):

        print('**** IMPORT INSTANCE ****')
        starts, goals, blank_start, blank_goal = import_instance(file)
        print('Starting Locations:')
        print_instance(starts)
        print('Goal Locations:')
        print_instance(goals)

        searches = ['A*', 'IDA*']
        paths = []
        for search in searches:
            print('**** Starting ' + search + ' Search ****')

            if search == 'A*':
                with futures.ThreadPoolExecutor(max_workers=1) as executor:
                    future = executor.submit(a_star, starts, goals, blank_start, blank_goal)
                    try:
                        path = future.result(time_out)
                    except futures.TimeoutError:
                        print('Timed out!')
                        paths.append(None)
                    else:
                        print('Finished ' + search)
                        paths.append(path)
                    executor._threads.clear()
                    futures.thread._threads_queues.clear()

            if search == 'IDA*':
                with futures.ThreadPoolExecutor(max_workers=1) as executor:
                    future = executor.submit(id_a_star, starts, goals)
                    try:
                        path = future.result(time_out)
                    except futures.TimeoutError:
                        print('Timed out!')
                        paths.append(None)
                    else:
                        print('Finished ' + search)
                        paths.append(path)
                    executor._threads.clear()
                    futures.thread._threads_queues.clear()
                    future.cancel()

        if not args.batch:
            for x in range(len(searches)):
                if paths[x] is None:
                    continue
                visualize_paths(paths[x], searches[x])
