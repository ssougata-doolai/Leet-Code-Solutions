class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        l = len(bloomDay)
        if l < m * k:
            return -1
        min_d = min(bloomDay)
        max_d = max(bloomDay)
        
        while min_d <= max_d:
            mid = (min_d + max_d) // 2
            k_c = 0
            m_c = 0
            for i in range(l):
                if bloomDay[i] <= mid:
                    k_c += 1
                else:
                    m_c += k_c // k
                    k_c = 0
            m_c += k_c // k
            if m_c >= m:
                max_d = mid - 1
            else:
                min_d = mid + 1

        return min_d


        # Brute forece
        # for i in range(min_d, max_d+1):
        #     k_c = 0
        #     m_c = 0
        #     for j in range(l):
        #         if bloomDay[j] <= i:
        #             k_c += 1
        #         else:
        #             m_c += k_c // k
        #             k_c = 0
        #     m_c += k_c // k
        #     if m_c >= m:
        #         return i