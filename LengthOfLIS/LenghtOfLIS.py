import pysnooper


class Solution(object):

    @staticmethod
    @pysnooper.snoop()
    def lengthOfLIS(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        array_lis = []
        max_length = 0
        for num in nums:
            if len(array_lis) == 0:
                array_lis.append([num, 1])
                max_length = 1
            else:
                temp_index_array = []
                max_index = -1
                max_len = 0
                for index, lis in enumerate(array_lis):
                    if array_lis[index][0] < num:
                        if array_lis[index][1] > max_len:
                            max_len = array_lis[index][1]
                            max_index = index
                if max_index >= 0:
                    length = array_lis[max_index][1]+1
                    array_lis.append([num, length])
                else:
                    length = 1
                    array_lis.append([num, 1])
                if length > max_length:
                    max_length = length

        return max_length


    @staticmethod
    @pysnooper.snoop()
    def lengthOfLIS2(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_length = 0
        if len(nums) > 0:
            dp_list = [1] * len(nums)
            for i in range(0, len(nums)):
                for j in range(0, i):
                    if nums[i] > nums[j]:
                        dp_list[i] = max(dp_list[i], dp_list[j]+1)
            max_length = max(dp_list)
        return max_length

if __name__ == '__main__':
    list_in = [10,9,2,5,3,7,101,18]
    print(Solution.lengthOfLIS2(list_in))
