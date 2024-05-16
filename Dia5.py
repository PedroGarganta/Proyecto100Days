######################### DIA 5 #############################
                                    
#Given an array nums of size n, return the majority element.

#The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array. 


#SOLUCION 1:
def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort();
        n= len(nums)
        return nums[n//2];

#SOLUCION 2(Funciona solo para listas pequeñas):

def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pos = -1;
        n = len(nums)/ 2
        encontrado = False

        while not encontrado:
                cantidad = 0
                pos +=1
                for i in range(0,len(nums)-1):
                        if (nums[i] == nums[pos]):
                                cantidad +=1
                                if (cantidad >= n):
                                        encontrado = True
                                        return nums[pos]
                        
#Solucion optima:

def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
                count = 1
            elif num == candidate:
                count += 1
            else:
                count -= 1

        # Verificar si el candidato es realmente el elemento mayoritario
        count = 0
        for num in nums:
            if num == candidate:
                count += 1
        if count > len(nums) / 2:
            return candidate
        else:
            return None                       