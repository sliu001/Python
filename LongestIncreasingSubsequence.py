#LC300: Given an integer array nums, return the length of the longest strictly increasing subsequence.
#
#Input: nums = [10,9,2,5,3,7,101,18]
#Output: 4
#Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
#
#Input: nums = [0,1,0,3,2,3]
#Output: 4
#
#lengthOfLIS_slow: O(n^2)
#lengthOfLIS_quick: O(nlogn)

class Solution:
    def lengthOfLIS_slow(self, nums: List[int]) -> int:
        res = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i-1, -1, -1):
                if nums[i] > nums[j]:
                    res[i] = max(res[i], res[j]+1)
            
        return max(res)
       
       
    def lengthOfLIS_quick(self, nums: List[int]) -> int:
        seq = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > seq[-1]:
                seq.append(nums[i])
            else:
                pos = self.findIdx(nums[i], seq)
                seq[pos] = nums[i]

        return len(seq)   
        
        
    def binarySearch(self, num: int, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = floor((left + right)/2)
            if num == nums[mid]:
                return mid
            elif num > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        
        return left        
