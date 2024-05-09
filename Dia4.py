##################################### DIA 4 #####################################

#Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

#Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

#Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.

#Return k.

def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j=1;
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[j] = nums[i];
                j += 1; 
        return j  



#Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

#Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

#Return k after placing the final result in the first k slots of nums.

#Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.


def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j= 1
        for i in range(1,len(nums)):
            if j == 1 or nums[i] != nums[j-2]:
                nums[j] = nums[i];
                j += 1;
        return j   