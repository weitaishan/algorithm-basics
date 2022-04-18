# *_*coding:utf-8 *_*
'''
旋转数组
给你一个数组，将数组中的元素向右轮转 k个位置，其中k是非负数。

示例 1:

输入: nums = [1,2,3,4,5,6,7], k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右轮转 1 步: [7,1,2,3,4,5,6]
向右轮转 2 步: [6,7,1,2,3,4,5]
向右轮转 3 步: [5,6,7,1,2,3,4]
示例2:

输入：nums = [-1,-100,3,99], k = 2
输出：[3,99,-1,-100]
解释:
向右轮转 1 步: [99,-1,-100,3]
向右轮转 2 步: [3,99,-1,-100]

提示：

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105


进阶：

尽可能想出更多的解决方案，至少有 三种 不同的方法可以解决这个问题。
你可以使用空间复杂度为O(1) 的原地算法解决这个问题吗？

'''
from typing import List
class Solution:
    '''
    方法一：数组翻转
    1.首先对整个数组实行翻转，这样子原数组中需要翻转的子数组，就会跑到数组最前面。
    2.这时候，从 kk 处分隔数组，左右两数组，各自进行翻转即可。
    '''
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        print(k)
        self.reverse(nums, 0, len(nums) - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len(nums) - 1)
    def reverse(self, nums, start, end) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    '''
    方法二：pop和insert
    '''
    def rotate2(self, nums: List[int], k: int) -> None:
        for i in range(k):
            nums.insert(0, nums.pop())

    '''
    方法三：切片翻转
    '''
    def rotate3(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]

solu = Solution()
nums = [1,2,3,4,5,6,7]
solu.rotate3(nums, 3)
print(nums)