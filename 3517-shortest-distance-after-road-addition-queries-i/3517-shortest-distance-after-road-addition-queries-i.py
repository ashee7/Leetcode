class Solution:
    def bfs(self,n,adjlist):
        visited=[False]*n
        nodequeue=deque()

        nodequeue.append(0)
        visited[0]=True

        currentlayernodecount=1
        nextlayernodecount=0
        layersexplored=0
        # print(adjlist)
        while nodequeue:
            for _ in range(currentlayernodecount):
                currentnode=nodequeue.popleft()
                if currentnode==n-1:
                    return layersexplored

                for neighbour in adjlist[currentnode]:
                    # print(visited)
                    if visited[neighbour]:
                        continue
                    nodequeue.append(neighbour)
                    nextlayernodecount+=1
                    visited[neighbour]=True
            currentlayernodecount=nextlayernodecount
            nextlayernodecount=0
            layersexplored+=1

        return -1

    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:

        answer=[]
        adjlist=[[] for _ in range(n)]
        for i in range(n-1):
            adjlist[i].append(i+1)
        
        for road in queries:
            # print(road)
            u,v=road
            adjlist[u].append(v)
            answer.append(self.bfs(n,adjlist))
        
        return answer
