import random
import os
import argparse

nums = []
sortedarray = []
sorts = 0
i = 1
target = 200
current = 0

fpath = __file__
absolute_path = os.path.abspath(fpath)
base_dir = os.path.dirname(absolute_path)
log_dir = base_dir + '/sorting_logs/'


def saveLog(array, target, sorts, shuffled):
    if not os.path.exists(log_dir):
        os.mkdir(log_dir)
    randint = random.randrange(100000,999999)
    log_file = log_dir + 'sort_' + str(target) + '_' + str(randint) + '.txt'
    if os.path.exists(log_file):
        saveLog(array, target)
    else:
        with open(log_file, "w") as file:
            file.write("Sort SUCCEEDED\n\n--  STATS --\n\nTARGET = " + str(target) + "\nSORTS = " + str(sorts) + "\n\n--  EO STATS  --\n\nFINAL ARRAY:\n\n\n" + str(sortedarray) + "\n\n\nSHUFFLED ARRAY:\n\n" + str(shuffled) + "\n\nmade by https://github.com/benjamint08")
            file.close()
            print("Saved to /sorting_logs/sort_" + str(target) + "_" + str(randint) + ".txt")


def find(current2, sortedarray2, nums2, target2, sorts):
    while not current2 == target2:
        for num in nums2:
            sorts = sorts + 1
            if num == current2 + 1:
                current2 = current2 + 1
                print(sortedarray2)
                sortedarray2.append(num)
                print(sortedarray2)
    print("Sort done. Saving to log file")
    saveLog(sortedarray2, target2, sorts, nums)


def start(i):
    while not i == target + 1:
        nums.append(i)
        i = i + 1
    print(nums)
    random.shuffle(nums)
    print(nums)
    find(current, sortedarray, nums, target, sorts)

parser = argparse.ArgumentParser()
parser.add_argument("-T", "--target", help="target number for sorting", type=int)
args = parser.parse_args()

if args.target:
    target = args.target
    start(i)
else:
    start(i)