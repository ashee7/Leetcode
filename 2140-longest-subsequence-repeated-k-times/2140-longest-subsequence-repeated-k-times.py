class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        ans=''

        queue=sorted([char for char,freq in Counter(s).items() if freq>=k],reverse=True)
        q=deque(queue)
        while q:
            curr=q.popleft()
            if len(curr)>len(ans):
                ans=curr
            for ch in queue:
                nxt=curr+ch
                it = iter(s)
                if all(ch in it for ch in nxt * k):
                    q.append(nxt)
        return ans

