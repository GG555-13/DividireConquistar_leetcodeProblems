from typing import List

class Solution:
    def mergeSkylines(self, left: List[List[int]], right: List[List[int]]) -> List[List[int]]:
        h1, h2 = 0, 0  
        i, j = 0, 0
        mergedsky = []
        
        while i < len(left) and j < len(right):
            if left[i][0] < right[j][0]:
                x = left[i][0]
                h1 = left[i][1]
                max_h = max(h1, h2)
                if not mergedsky or mergedsky[-1][1] != max_h:
                    mergedsky.append([x, max_h])
                i += 1
            elif left[i][0] > right[j][0]:
                x = right[j][0]
                h2 = right[j][1]
                max_h = max(h1, h2)
                if not mergedsky or mergedsky[-1][1] != max_h:
                    mergedsky.append([x, max_h])
                j += 1
            else:
                x = left[i][0]
                h1 = left[i][1]
                h2 = right[j][1]
                max_h = max(h1, h2)
                if not mergedsky or mergedsky[-1][1] != max_h:
                    mergedsky.append([x, max_h])
                i += 1
                j += 1
        
        while i < len(left):
            mergedsky.append(left[i])
            i += 1
        
        while j < len(right):
            mergedsky.append(right[j])
            j += 1
        
        return mergedsky
    
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        if not buildings:
            return []
        if len(buildings) == 1:
            left, right, height = buildings[0]
            return [[left, height], [right, 0]]
        
        mid = len(buildings) // 2
        leftsky = self.getSkyline(buildings[:mid])
        rightsky = self.getSkyline(buildings[mid:])
        
        return self.mergeSkylines(leftsky, rightsky)

def test():
    solution = Solution()
    
    ct = [
        (
            [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]],
            [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]]
        ),
        (
            [[0, 2, 3], [2, 5, 3]],
            [[0, 3], [5, 0]]
        ),  
        (
            [[1, 2, 1], [1, 2, 2], [1, 2, 3]],
            [[1, 3], [2, 0]]
        ),  
        (
            [[1, 5, 3], [2, 7, 4], [3, 9, 5]],
            [[1, 3], [2, 4], [3, 5], [9, 0]]
        ),  
        (
            [[0, 1, 3], [1, 2, 3], [2, 3, 3]],
            [[0, 3], [3, 0]]
        ),
    ]
    
    for i, (buildings, expected) in enumerate(ct):
        result = solution.getSkyline(buildings)
        print(f"Test case {i + 1}: buildings = {buildings}")
        print(f"Result: {result}")
        print(f"Expected: {expected}\n")

if __name__ == "__main__":
    test()
