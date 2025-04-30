class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        def total(k):
            ret = 0
            for i in piles:
                ret += math.ceil(i/k)
            return ret

        while l < r:
            m = (l + r) // 2
            if total(m) <= h: # 최소값 찾기니까 == 인 경우에도 더 최소인 값을 찾아보자
                r = m # 정답이 m일 수도 있기 때문에
            else:
                l = m + 1
        return l