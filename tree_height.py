# python3

import sys
import threading


def compute_height(n, parents):
    max_height = {}
    
    def get_height(node):
        if node in max_height:
            return max_height[node]
        if parents[node] == -1:
            max_height[node] = 1
            return 1
        
        height = get_height(parents[node]) + 1
        max_height[node] = height
        return height
    
    return max(get_height(node) for node in range(n))

def main():
    while True:
        try:
            input_variant = input()
        except EOFError:
            return
        if "I" in input_variant:
            n = int(input())
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
