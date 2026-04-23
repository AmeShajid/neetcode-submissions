class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # goal: find all unique triplets that sum to 0
        result = []
        nums.sort()  # sort to use two-pointer strategy

        # iterate over each number (this will be the "fixed" number)
        for index, value in enumerate(nums):
            # skip duplicates for the fixed number
            if index > 0 and value == nums[index - 1]:
                continue

            # two pointers
            left = index + 1
            right = len(nums) - 1

            while left < right:
                threesum = value + nums[left] + nums[right]

                if threesum > 0:
                    # sum too large, move right pointer left
                    right -= 1
                elif threesum < 0:
                    # sum too small, move left pointer right
                    left += 1
                else:
                    # found a valid triplet
                    result.append([value, nums[left], nums[right]])

                    # move both pointers inward
                    left += 1
                    right -= 1

                    # skip duplicates on the left side
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    # skip duplicates on the right side
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return result

        