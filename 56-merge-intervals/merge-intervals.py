class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: (x[0], x[1]))
        print(intervals)

        new_list = []
        l = len(intervals)
        if l <= 1:
            return intervals

        prev0 = intervals[0][0]
        prev1 = intervals[0][1]

        for i in range(1, l):
            next0 = intervals[i][0]
            next1 = intervals[i][1]

            if next0 <= prev1:
                if prev1 < next1:
                    prev1 = next1
            else:
                new_list.append([prev0, prev1])
                prev0 = next0
                prev1 = next1
        new_list.append([prev0, prev1])

        return new_list
        
        # new_list = []
        # l = len(intervals)
        # if l <= 1:
        #     return intervals

        # prev0 = intervals[0][0]
        # prev1 = intervals[0][1]
        # for i in range(1, l):
        #     next0 = intervals[i][0]
        #     next1 = intervals[i][1]

        #     # case 1: [5, 6], [4, 7]
        #     if prev0 >= next0 and prev1 <= next1:
        #         print("1")
        #         prev0 = next0
        #         prev1 = next1

        #     # case 2: reverse [4, 7], [5, 6]
        #     elif prev0 <= next0 and prev1 >= next1:
        #         print("2")

        #     # case 3: overlapping
        #     elif prev1 >= next0 and prev1 <= next1:
        
        # new_list.append([prev0, prev1])
        # return new_list
                