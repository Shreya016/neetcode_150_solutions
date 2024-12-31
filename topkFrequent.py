import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency={}
        heap=[]
        for num in nums:
          if num not in frequency:
            frequency[num] =1
          else:
            frequency[num] +=1
        for num,freq in frequency.items():
          heapq.heappush(heap,(freq,num))
          if len(heap)>k:
            heapq.heappop(heap)
        return [num for freq, num in heap]