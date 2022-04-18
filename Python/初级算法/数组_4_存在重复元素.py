# *_*coding:utf-8 *_*
'''
存在重复元素
给你一个整数数组 nums 。如果任一值在数组中出现 至少两次 ，返回 true ；如果数组中每个元素互不相同，返回 false 。

示例 1：

输入：nums = [1,2,3,1]
输出：true
示例 2：

输入：nums = [1,2,3,4]
输出：false
示例3：

输入：nums = [1,1,1,3,3,4,3,2,4,2]
输出：true

提示：

1 <= nums.length <= 105
-109 <= nums[i] <= 109

'''

from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        '''
        方法一：先排序，然后在依次比较
        复杂度分析
        时间复杂度：O(NlogN)，其中 N 为数组的长度。需要对数组进行排序。
        空间复杂度：O(logN)，其中 N 为数组的长度。注意我们在这里应当考虑递归调用栈的深度。
        '''
        if len(nums) <= 1:
            return False
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False

    def containsDuplicate2(self, nums: List[int]) -> bool:
        # 方法二：使用集合，判断长度
        if len(set(nums)) != len(nums):
            return True
        return False

    def containsDuplicate3(self, nums: List[int]) -> bool:
        '''
        方法三：哈希表
        复杂度分析
        时间复杂度：O(N)，其中 N 为数组的长度。
        空间复杂度：O(N)，其中 N 为数组的长度。
        '''
        s = set()
        for i in nums:
            if i in s:
                return True
            s.add(i)
        return False


nums = [1,2,3,4,1]
print(Solution().containsDuplicate3(nums))
