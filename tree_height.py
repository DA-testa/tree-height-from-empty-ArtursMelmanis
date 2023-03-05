# python3

import sys
import threading


def compute_height(n, parents):
    max_height = 0
    
    for x in range (n):
        height = 0
        while x != 1:
            level += 1
            x = parents[x]
        max_height = max(max_height, level)
    return max_height


def main():
    while True:
        try:
            input_variant = input()
        except EOFError:
            return
        if "I" in input_variant:
            n = input()
            parents = list(map(int, input().split()))
            print(compute_height(n, parents))
            break
        if "F" in input_variant:
            file_var = "test/" + input()
            if "a" in file_var:
                return
            try:
                with open(file_var) as file:
                    n = int(file.readline())
                    parents = list(map(int, file.readline().split()))
                    print(compute_height(n, parents))
                    break
            except FileNotFoundError:
                return

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
# print(numpy.array([1,2,3]))
