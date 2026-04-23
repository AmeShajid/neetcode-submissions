class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #storage for the last seen nubmers 
        storage = {}

        #iterate through nums
        for i in range(len(nums)):
            #if the value is in stroage
            if nums[i] in storage:
                #if the index - nums[i] -> value then storage[value] <= k
                if i - storage[nums[i]] <= k:
                    #return True
                    return True

            # ALWAYS update last seen index
            #so now nums[i] -> value -> storage[value] update the index to the current index
            storage[nums[i]] = i
        #return false
        return False