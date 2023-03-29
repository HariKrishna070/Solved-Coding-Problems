"""
QUESTION : Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109

"""

#solution:

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1,-1]
        c = nums.count(target)
        if(len(nums) == 0 or c == 0):
            return ans
        elif(len(nums)==1 and nums[0]==target):
            ans = [0,0]
        else:
            ans[0]=nums.index(target)
            ans[1]=ans[0]+c-1
        return ans
