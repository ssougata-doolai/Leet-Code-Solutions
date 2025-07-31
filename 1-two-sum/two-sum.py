class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        d = {}
        flag = False
        newNums = []
        for i in nums:
            d[i] = i

        for key, value in d.items():
            try:
                n2 = d[target - key]
                n1 = value
                flag = True
                if n1 != n2:
                    break
            except:
                pass
        
        for i in range(l):
            if nums[i] == n1 or nums[i] == n2:
                newNums.append(i)

        return newNums


        # Brute force approach
        # l = len(nums)
        # newNums = []
        # for i in range(l):
        #     for j in range(i+1, l):
        #         if nums[i] + nums[j] == target:
        #             newNums.append(i)
        #             newNums.append(j)
        #             return newNums
