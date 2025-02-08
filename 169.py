
# My solution
class Solution(object):
    def majorityElement(self, nums):
        a = {}
        for i in nums:
            if i not in a:
                a[i] = 1
            else:
                a.update({i: a.get(i) + 1})
        max_key = max(a, key=a.get)
        return max_key

# Better Solution
# class Solution(object):
#    def majorityElement(self, nums):
#      return max(set(nums), key=nums.count)
