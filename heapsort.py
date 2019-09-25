import sys

# method to build max heap
def build_max_heap(array):
    # call max heapify on length/2 in reverse order
    for x in list(reversed(xrange(len(array)/2))):
        max_heapify(array, x)


# method to max heapify
def max_heapify(array, index):
    # variables to define
    length = len(array)
    parent = array[index]
    child_left = None
    child_right = None
    largest = parent
    largest_index = index

    # if the index exists, set child
    if left(index) < length: 
        child_left = array[left(index)]
    if right(index) < length: 
        child_right = array[right(index)]

    # find the largest index among children and parent 
    if child_left and child_left > largest:
        largest = child_left
        largest_index = left(index)
    if child_right and child_right > largest:
        largest = child_right
        largest_index = right(index) 

    # if parent is not largest, swap then rerun on the place it swapped to
    if largest_index != index:
        array[index] = largest
        array[largest_index] = parent
        max_heapify(array, largest_index)

# method to heapsort
def heapsort(array):
    # build max heap
    build_max_heap(array)
    
    # array for popped values
    sorted_array = []

    # while there are values in the array reheap, swap, then pop
    while len(array):
        max_heapify(array, 0)
        print("Heap after heapify: %s, What has been popped from heap: %s" % (array, sorted_array))
        swap(array)
        print("Swapping... Heap after swap: %s\n" % (array))
        sorted_array.insert(0, array.pop())
    print("\nFinal sorted array: %s" % (sorted_array))

#method to swap first and last element of array
def swap(array):
    if len(array) == 1:
        return
    temp = array.pop()
    array.append(array[0])
    array[0] = temp
    return

# method to return the left child index
def left(i):
    return 2*i+1;

# method to return the right child index
def right(i):
    return 2*(i+1);

# exit if a list was not given
if not len(sys.argv) > 1:
    print("usage: python " + sys.argv[0], " <comma seperated list>")
    exit(1)

# init an array and add the string to it
array = []
for x in sys.argv[1].split(','):
    array.append(int(x))

# run the heapsort
heapsort(array)
