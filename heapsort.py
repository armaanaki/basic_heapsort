import sys

def build_max_heap():
    return 0
def max_heapify():
    return 0
def heapsort():
    return 0

# exit if a list was not given
if not len(sys.argv) > 1:
    print("usage: python " + sys.argv[0], " <comma seperated list>")
    exit(1)

# init an array and add the string to it
array = []
for x in sys.argv[1].split(','):
    array.append(int(x))
