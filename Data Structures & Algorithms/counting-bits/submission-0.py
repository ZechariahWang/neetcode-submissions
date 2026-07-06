class Solution:
    def countBits(self, n: int) -> List[int]:
        dp=[0]*(n+1)
        offset=1

        for i in range(n+1):
            if i==0:
                dp[0]=0
                continue
            elif offset*2==i:
                offset=i
            dp[i]=1+dp[n-offset]
        return dp