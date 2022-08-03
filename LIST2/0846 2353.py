from sortedcontainers import SortedList
from sortedcontainers import SortedDict


class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.dic = {}
        self.way = {}
        n = len(foods)
        for i in range(n):
            f = foods[i]
            c = cuisines[i]
            r = ratings[i]

            self.way[f] = (c, r)

            if c not in self.dic:
                self.dic[c] = SortedDict()
            if -r not in self.dic[c]:
                self.dic[c][-r] = SortedList()
            self.dic[c][-r].add(f)

    def changeRating(self, food: str, newRating: int) -> None:
        c, r = self.way[food]
        # print(self.dic[c][-r],c,r)
        self.dic[c][-r].remove(food)
        if len(self.dic[c][-r]) == 0:
            self.dic[c].pop(-r)
        if -newRating not in self.dic[c]:
            self.dic[c][-newRating] = SortedList()
        self.dic[c][-newRating].add(food)
        self.way[food] = (c, newRating)

    def highestRated(self, cuisine: str) -> str:
        r = self.dic[cuisine].keys()[0]
        m = self.dic[cuisine][r][0]
        return m

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)