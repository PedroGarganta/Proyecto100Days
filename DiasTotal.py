###################### DIA 6 ##################################
# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        tot= len(nums)
        for i in range(k):
                ultimo = nums[tot];
                for j in range(0,tot):
                         nums[tot-j]= nums[tot-j-1]
                nums[0]= ultimo;


