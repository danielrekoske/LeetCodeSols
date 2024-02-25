class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        if not nums:
          return index
        else:
          for i in range(0, len(nums)):
              if nums[i] != val:
                  nums[index] = nums[i]
                  index += 1
        return index 