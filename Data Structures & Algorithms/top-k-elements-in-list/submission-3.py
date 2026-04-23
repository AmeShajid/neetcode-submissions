class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #dictionary for keeping count
        count = {}
        #we want to get the frequency of our nums
        #iterate through nums
        for num in nums:
            #update the count
            #add 1 to the num value and theres nothing do 0
            count[num] = 1 + count.get(num,0)
        print(count)

        heap = []
        for num, frequency in count.items():
            heapq.heappush(heap, (-frequency , num))
        print(heap)

        result = []
        for i in range(k):
            temp = heapq.heappop(heap)
            result.append(temp[1])
        return result
            





