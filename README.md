# CMPT 417 Group Project

## Overview

Implement searches that will solve tile puzzles ranging from 3x3s to 5x5s. The searches that will be implemented will be A*, IDA*, IDDFS, DACA*

A* was adapted from the code provided for our individual project.

IDA* as referenced and adapted from [here.](https://en.wikipedia.org/wiki/Iterative_deepening_depth-first_search)

IDDFS as referenced and adapted from [here.](https://doi.org/10.1016/0004-3702(85)90084-0)

DACA* as referenced and adapated from [here.](https://www.kopf.com.br/kaplof/how-to-solve-any-slide-puzzle-regardless-of-its-size/)

## Test Instances

For our searches, we ran them with the following instances.

- Test 1 - 3 are 3x3 tile puzzles.
- Test 4 - 6 are 3x4 tile puzzles.
- Test 7 - 9 are 4x4 tile puzzles.
- Test 9 - 12 are 4x5 tile puzzles.
- test 13 - 15 are 5x5 tile puzzles.

## How to Test

### For individual instance testing with graphics:
> python run_experiments.py --instance "instances/test_x.txt" --solver CBS

**NOTE:** Replace 'x' with instance number.

### For batch instance testing without graphics:
> python run_experiments.py --instance "instances/test_*" --solver CBS --batch
