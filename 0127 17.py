class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        dic = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        res = [""]
        for num in digits:
            neores = []
            for alpha in dic[num]:
                neo = res.copy()
                for x in range(len(neo)):
                    neo[x] = neo[x] + alpha
                neores.extend(neo)
            res = neores
        return res