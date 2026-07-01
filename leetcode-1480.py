class Solution(object):
    def runningSum(self, nums):
        num=[1,3,7,10]
        a=0
        b=[]
        for i in nums:
            a=i+a
            b.append(a)
        return b