class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        answer = []
        prefix = ""
        for ch in searchWord:
            prefix += ch
            index = bisect_left(products, prefix)
            suggestions = []
            for i in range(index, min(index + 3, len(products))):
                if products[i].startswith(prefix):
                    suggestions.append(products[i])
            answer.append(suggestions)
        return answer