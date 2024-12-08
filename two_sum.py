class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices_dic={}
        for i, num in enumerate(nums):
            j=target-num
            if j in indices_dic:
                return [indices_dic[j],i]
            else:
                indices_dic[num]=i