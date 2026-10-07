class Solution:
    def maxIceCream(self, costs: list[int], coins: int) -> int:
        costs.sort()
        ans=0
        took=0
        for n in costs:
            if n<=coins:
                took+=n
                ans+=1
                coins-=n
        return ans