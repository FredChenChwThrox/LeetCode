import pysnooper


class Solution(object):

    @staticmethod
    @pysnooper.snoop()
    def wordPattern(pattern, string):
        """
        :type pattern: str
        :type string: str
        :rtype: bool
        """
        pattern_map = {}
        string_array = string.split(' ')
        if len(string_array) == len(pattern):
            for index, char in enumerate(pattern):
                if char in pattern_map.keys():
                    if string_array[index] != pattern_map[char]:
                        return False
                else:
                    if string_array[index] not in pattern_map.values():
                        pattern_map[char] = string_array[index]
                    else:
                        return False

            return True
        return False


if __name__ == '__main__':
    Solution.wordPattern("aabb", "Cat Cat Cat Cat")

