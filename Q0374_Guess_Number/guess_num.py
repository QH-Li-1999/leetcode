# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        start, end = 1, n
        while(start <= end):
            mid = (start + end)//2
            flag = guess(mid)
            if flag > 0: start = mid + 1
            elif flag == 0: return mid
            else: end = mid - 1
        return -1
        """
        :type n: int
        :rtype: int
        """
        
