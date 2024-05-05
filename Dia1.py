#############   DIA 1  #############

# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.


def juntarArrays (num1, m, num2,n):
    i=m-1;
    j=n-1;
    k=m+n-1;
    while(j>=0):
        if(i>=0) and num1[i]>num2[j]:
            num1[k]= num1[i];
            i-=1;
        else: 
            num1[k]= num2[j];
            j-=1;
        print(num1)
        k-=1;
        

    

array1=[1,2,3,0,0,0];
array2=[2,3,4];
juntarArrays(array1,3,array2,3)

        
       