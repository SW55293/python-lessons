from ast import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []

        def dfs(x, current, total):
            if total == target:
                results.append(current.copy())
                return
            if x >= len(candidates) or total > target:
                return

            current.append(candidates[x])
            dfs(x, current, total + candidates[x])
            current.pop()
            dfs(x + 1, current, total)
    

        dfs(0, [], 0)

        return results
