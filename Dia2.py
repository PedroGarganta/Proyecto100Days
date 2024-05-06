################################ DIA 2 ################################ 


#Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

#Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

#Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.

#Return k.

def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        for i in range(0,len(nums)):
                if nums[i] == val :
                        nums[i] == '_'
        nums.sort()
        for i in range(0,len(nums)):
                if nums[i] != '_':
                        contador +=1;
        return contador;



# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

def strStr(haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        pos = 0;
        contador = 0;
        for i in range(0,len(haystack)-len(needle)+1):
                if(haystack[i] == needle[0]):
                        pos = i;
                        print(pos)
                        contador = 0;
                        for j in range(0,len(needle)):
                                if haystack[i+j] == needle[j]:
                                    contador +=1;
                                if contador == len(needle):
                                    return pos;
        if (contador != len(needle)):
            return -1             
        



