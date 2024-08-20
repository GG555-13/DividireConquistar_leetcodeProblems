from typing import List

class Solution:
    def merge(self, nums, start, mid, end):
        temp = []
        i, j = start, mid + 1
        while i <= mid and j <= end:
            if nums[i] <= nums[j]:
                temp.append(nums[i])
                i += 1
            else:
                temp.append(nums[j])
                j += 1
        while i <= mid:
            temp.append(nums[i])
            i += 1
        while j <= end:
            temp.append(nums[j])
            j += 1
        
        for i in range(len(temp)):
            nums[start + i] = temp[i]

    def merge_sort(self, nums, start, end):
        if start >= end:
            return 0
        
        mid = (start + end) // 2
        count = self.merge_sort(nums, start, mid) + self.merge_sort(nums, mid + 1, end)
        
        j = mid + 1
        for i in range(start, mid + 1):
            while j <= end and nums[i] > 2 * nums[j]:
                j += 1
            count += j - (mid + 1)
        
        self.merge(nums, start, mid, end)
        return count

    def reversePairs(self, nums: List[int]) -> int:
        return self.merge_sort(nums, 0, len(nums) - 1)

def teste():
    solution = Solution()
    
    ct = [
        ([1, 2, 3, 4, 5], 0),  
        ([2, 4, 3, 5, 1], 3),  
        ([5, 4, 3, 2, 1], 4),  
        ([100000000, 10000000, 1000000, 100000, 10000], 10),  
        ([1, 1, 1, 1, 1], 0),  
    ]
    
    for i, (nums, expected) in enumerate(ct):
        result = solution.reversePairs(nums)
        print(f"Test case {i + 1}: nums = {nums}")
        print(f"Result: {result}")
        print(f"Expected: {expected}\n")

if __name__ == "__main__":
    teste()