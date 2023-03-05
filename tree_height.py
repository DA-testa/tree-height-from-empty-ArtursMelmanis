# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    root = parents.index(-1)
    max_height = 0
    stack = [(root, 1)]
    
    while stack:
        node, level = stack.pop()
        max_height = max(max_height, level)
        children = [i for i, p in enumerate(parents) if p == node]
        stack.extend([(c, level+1) for c in children])
    return max_height


def main():
    while True:
        input_variant = input()
        if input_variant == "I":
            n = input()
            parents = list(map(int, input().split()))
            break
        if input_variant == "F":
            file_var = input()
            if "a" in file_var:
                return 1
            try:
                with open("./test/" + file_var, input_variant = 'r') as file:
                    n = int(file.readline())
                    parents = list(map(int, file.readline().split()))
                    break
            except FileNotFoundError:
                return 1
        else:
            print("Nepareizi ievadīts formats")
    max_height = compute_height(n,parents)
    print(max_height)
    return 0

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
# print(numpy.array([1,2,3]))
