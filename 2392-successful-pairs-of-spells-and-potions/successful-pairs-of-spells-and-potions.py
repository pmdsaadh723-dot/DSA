class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        total = len(potions)
        answer = []
        for spell in spells:
            need = (success + spell - 1) // spell
            index = bisect_left(potions, need)
            answer.append(total - index)
        return answer