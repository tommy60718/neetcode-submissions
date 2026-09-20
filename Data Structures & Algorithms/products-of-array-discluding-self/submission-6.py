class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #nums = [1,2,4,6]
        # prefix = [1, 1, 2, 8] 
        # sufix = [48, 24, 6, 1]
        prefix_mul= []
        sufix_mul= []

        #prefix
        for i in range(len(nums)):
            if i ==0 : prefix_mul.append(1)
            else:
                prefix_mul.append(prefix_mul[i-1] * nums[i-1])
        print(prefix_mul)
        #sufix
        rev_nums=nums[::-1]
        rev_sufix=[]
        for i in range(len(nums)):
            if i==0: rev_sufix.append(1)
            else:
                rev_sufix.append(rev_sufix[i-1] * rev_nums[i-1])
        sufix_mul = rev_sufix[::-1]
        print(sufix_mul)

        res=[]
        for i in range(len(nums)):
            res.append(sufix_mul[i] * prefix_mul[i])
        return res