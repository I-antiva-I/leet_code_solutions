# LeetCode #0039 | Combination Sum | [MEDIUM]

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        combos = []
        combo = []
        candidates.sort()

        def makeCombo(combo, start):
            if sum(combo) == target:
                combos.append([c for c in combo])
                return True

            elif sum(combo) > target:
                return True

            else:
    
                for i in range(start, len(candidates)):
                    combo.append(candidates[i])
                    if makeCombo(combo, i):
                        combo.pop()
                        break
                    combo.pop()
                return False

        makeCombo(combo, 0)
        return combos