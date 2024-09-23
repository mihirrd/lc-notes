'''
Given an array of integers nums and an integer target, return `indices` of the two numbers,
such that they add up to target.
'''

# when list is not sorted
# uses O(n) space, O(n) time.
def findpair(nums: list[int], target: int) -> list[int]:
    visited = {} # stores elements and their indices
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in visited:
            return [visited[diff], i]
        else:
            visited[nums[i]] = i
    