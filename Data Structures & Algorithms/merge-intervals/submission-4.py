class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # [1, 5], [5, 7], [2,4]
        # Target: Merge "crossed" intervals together.
        # Core: We care the "crossed" 
        # Sol: -> Sort them according to start time
            # Deside to append or merge.
        intervals.sort(key = lambda pair : pair[0])
        output = [intervals[0]]

        for start, end in intervals[1:]:
            # Edge 1: [1, 3], [3, 5]
            # Sol: use >=
            if output[-1][1] >= start:
                # Edge 2: [1, 5], [2, 4]
                # Sol: use "max"
                output[-1][1] = max(output[-1][1], end)
            else:
                output.append([start, end])
        return output
            