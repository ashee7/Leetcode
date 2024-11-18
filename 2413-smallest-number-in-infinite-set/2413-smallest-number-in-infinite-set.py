import heapq 

class SmallestInfiniteSet:

    def __init__(self):
        self.heap=[]
        # self.present=set()
        self.current=1

    def popSmallest(self) -> int:
        if self.heap:
            smallest=self.heap[0]
            while self.heap and self.heap[0]==smallest:
                smallest=heapq.heappop(self.heap)
        else:
            smallest=self.current
            self.current+=1

        return smallest

    def addBack(self, num: int) -> None:
        if num<self.current:
            heapq.heappush(self.heap,num)
            



# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)