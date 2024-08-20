from collections import Counter
from typing import List

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        def dvc(start, end):
            if end - start + 1 < k:  
                return 0
            
            count = Counter(s[start:end + 1])
            
            for mid in range(start, end + 1):
                if count[s[mid]] < k:
                    left = dvc(start, mid - 1)
                    right = dvc(mid + 1, end)
                    return max(left, right)
            
            return end - start + 1
        
        return dvc(0, len(s) - 1)

def teste():
    solution = Solution()
    
    ct = [
        ("aaabb", 3, 3),  
        ("ababbc", 2, 5),  
        ("aaabbbccc", 3, 9),  
        ("aabb", 3, 0),  
        ("abcde", 2, 0),  
    ]
    
    for i, (s, k, expected) in enumerate(ct):
        result = solution.longestSubstring(s, k)
        print(f"Test case {i + 1}: s = {s}, k = {k}")
        print(f"Result: {result}")
        print(f"Expected: {expected}\n")

if __name__ == "__main__":
    teste()