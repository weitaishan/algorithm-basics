# *_*coding:utf-8 *_*

"""

给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9

所以返回 [0, 1]

"""

class Solution(object):

    #直接双循环遍历判断 时间复杂度O( n^2 )
    def twoSum(self, nums, target):
        for index1, value1 in enumerate(nums):
            for index2, value2 in enumerate(nums):
                if value1 + value2 == target:
                    return [index1,index2]


    """
    使用查找表来解决该问题。

设置一个 map 容器 record 用来记录元素的值与索引，然后遍历数组 nums。

每次遍历时使用临时变量 complement 用来保存目标值与当前值的差值
在此次遍历中查找 record ，查看是否有与 complement 一致的值，如果查找成功则返回查找值的索引值与当前变量的值 i
如果未找到，则在 record 保存该元素与索引值 i

    """
    def twoSum2(self, nums, target):
        record = {}
        for index, value in enumerate(nums):
            complement = target - value
            if complement in record:
                return [record[complement], index]
            record[value] = index
        return None

solution = Solution()
nums = [2,31,7,11,15]
target = 9
list = solution.twoSum2(nums,target)
print(list)

"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""