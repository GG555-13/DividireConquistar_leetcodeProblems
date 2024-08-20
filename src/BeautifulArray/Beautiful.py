from typing import List

class Solution:
    def beautifulArray(self, N: int) -> List[int]:
        def dvc(nums: List[int]) -> List[int]:
            if len(nums) <= 2:
                return nums
            
            even = dvc(nums[::2])
            odd = dvc(nums[1::2])
            
            return even + odd
        
        return dvc(list(range(1, N + 1)))

def teste():
    solution = Solution()
    
    ct = [
        (5, [1, 5, 3, 2, 4]),
        (6, [1, 5, 3, 2, 6, 4]),
        (7, [1, 5, 3, 7, 2, 6, 4]),
        (8, [1, 5, 3, 7, 2, 6, 4, 8]),
        (9, [1, 9, 5, 3, 7, 2, 6, 10, 4, 8]),
        (10, [1, 9, 5, 13, 3, 11, 7, 15, 2, 10, 6, 14, 4, 12, 8]),
    ]
    
    for i, (N, expected) in enumerate(ct):
        result = solution.beautifulArray(N)
        print(f"Test case {i + 1}: N = {N}")
        print(f"Result: {result}")
        print(f"Expected: {expected}\n")

if __name__ == "__main__":
    teste()
