# *_*coding:utf-8 *_*
'''
只出现一次的数字
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:

输入: [2,2,1]
输出: 1
示例2:

输入: [4,1,2,1,2]
输出: 4
'''
from typing import List
from functools import reduce
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        newNums = []
        # 通过将重复的元素删除，剩下的就是只出现一次的元素
        for i in range(len(nums)):
            if nums[i] in newNums:
                newNums.remove(nums[i])
            else:
                newNums.append(nums[i])
        return newNums[0]

    def singleNumber2(self, nums: List[int]) -> int:
        # 先排序，如果一个元素跟相邻的元素都不同，则那个元素就是只出现一次的元素
        if len(nums) == 1:
            return nums[0]
        nums.sort()
        for i in range(len(nums)):
            if i == 0 and nums[i] != nums[i+1]:
                return nums[0]
            if i == len(nums) - 1 and nums[i] != nums[i-1]:
                return nums[-1]
            if nums[i-1] != nums[i] and nums[i] != nums[i+1]:
                return nums[i]

    # 看解析，最好的方法
    def singleNumber3(self, nums: List[int]) -> int:
        # 异或运算
        # result = 0
        # for i in range(len(nums)):
        #     result ^= nums[i]
        # return result
        return reduce(lambda x, y: x ^ y, nums)

    def singleNumber4(self, nums: List[int]) -> int:
        # 使用哈希表存储每个数字和该数字出现的次数。遍历数组即可得到每个数字出现的次数，并更新哈希表，最后遍历哈希表，得到只出现一次的数字。
        result = {}
        for i in range(len(nums)):
            if nums[i] in result:
                result[nums[i]] += 1
            else:
                result[nums[i]] = 1

        for k,v in result.items():
            if v == 1:
                return k

    def singleNumber5(self, nums: List[int]) -> int:
        # 使用集合存储数组中出现的所有数字，并计算数组中的元素之和。由于集合保证元素无重复，因此计算集合中的所有元素之和的两倍，即为每个元素出现两次的情况下的元素之和。由于数组中只有一个元素出现一次，其余元素都出现两次，因此用集合中的元素之和的两倍减去数组中的元素之和，剩下的数就是数组中只出现一次的数字。
        return sum(set(nums)) * 2 - sum(nums)

nums = [4,1,2,1,2]
print(8^8)
print(Solution().singleNumber3(nums))