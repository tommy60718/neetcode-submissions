class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # build a dict, {key, value} = {element, frequency}
        keydict = defaultdict(int)

        #Count the frequency of letter for each element
        for num in nums:
            keydict[num] += 1
        #Sort the dictionary according to value
        sorted_keys =  sorted (keydict.keys(), key=lambda x:keydict[x], reverse = True)

        #return the top k frequent element
        return sorted_keys[:k]