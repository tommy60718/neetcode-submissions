class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key = lambda pair : pair[0])
        output = [intervals[0]]

        for start, end in intervals[1:]:
            if output[-1][1] >= start:
                # Take care of edge case: use "max"
                # [1, 5], [2, 4]
                output[-1][1] = max(output[-1][1], end)
            else:
                output.append([start, end])
        return output
            