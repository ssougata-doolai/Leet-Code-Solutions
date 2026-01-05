class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter
        freq = Counter(s)

        sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        # print(sorted_freq)

        s = []
        for ch, fre in sorted_freq:
            s.append(ch * fre)
        
        return "".join(s)