class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:        
        # res = list[list[int]]
        res = []

        # index: fix, remaining = two sum
        # two sum index: fix_fix, moving
        ## The magic of the opertaion: 
        ## We add new pair only after we check original dictionary <-
        ## -> We will never fetch "itself" as the answer.
        for i, fix in enumerate(nums):
            two_dict = {} # {value: index}
            for j, fix_fix in enumerate(nums[i+1:]):
                # fix + fix_fix + moving = 0
                # -> moving = -fix -fix_fix
                if (-fix-fix_fix) in two_dict:
                    res.append([fix, fix_fix, -fix-fix_fix])
                two_dict[fix_fix] = j
        
        #check duplicate
        #res_set = set(list[int])
        res_set = set()
        #for i in range(res):
        for i in range(len(res)):
            res[i].sort()
            #res_set.append(res[i])
            res_set.add(tuple(res[i]))
        final_res =[]
        for triplet in res_set:
            final_res.append(list(triplet))
        return final_res