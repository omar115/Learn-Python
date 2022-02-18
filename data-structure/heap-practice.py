'''
finding the largest N-smallest and
N-largest number in a list
'''
import heapq
import timeit

nums = [1, 6, 2, 8, -4, 18, 32, 2]
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))