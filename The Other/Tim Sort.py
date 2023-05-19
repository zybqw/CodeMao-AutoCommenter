from time import *
from random import *
def binary_search(the_array, item, start, end):#二分法插入排序
    if start == end:
        if the_array[start] > item:
            return start
        else:
            return start + 1
    if start > end:
        return start
    mid = round((start + end)/ 2)
    if the_array[mid] < item:
        return binary_search(the_array, item, mid + 1, end)
    elif the_array[mid] > item:
        return binary_search(the_array, item, start, mid - 1)
    else:
        return mid

def insertion_sort(the_array):
    l = len(the_array)
    for index in range(1, l):
        value = the_array[index]
        pos = binary_search(the_array, value, 0, index - 1)
        the_array = the_array[:pos] + [value] + the_array[pos:index] + the_array[index+1:]
    return the_array

def merge(left, right):#归并排序
    if not left:
        return right
    if not right:
        return left
    if left[0] < right[0]:
        return [left[0]] + merge(left[1:], right)
    return [right[0]] + merge(left, right[1:])

def timSort(the_array):
    runs, sorted_runs = [], []
    length = len(the_array)
    new_run = []
    for i in range(1, length):#将序列分割成多个有序的run
        if i == length - 1:
            new_run.append(the_array[i])
            runs.append(new_run)
            break
        if the_array[i] < the_array[i-1]:
            if not new_run:
                runs.append([the_array[i-1]])
                new_run.append(the_array[i])
            else:
                runs.append(new_run)
                new_run = []
        else:
            new_run.append(the_array[i])
    for item in runs:
        sorted_runs.append(insertion_sort(item))
    sorted_array = []
    for run in sorted_runs:
        sorted_array = merge(sorted_array, run)
    print(sorted_array)

arr = [randint(0,1000)for i in range(1000)]
t0 = perf_counter()
timSort(arr)
t1 = perf_counter()
print('共%.5f秒' %(t1-t0))
