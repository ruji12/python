# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).


num = [0,2,4,5,10,17]
n = len(num)
arr=[0]*(n)
sum=0


for i in range(n):
   sum +=num[i]
   arr[i]=sum

print(arr)
    