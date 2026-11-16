class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Case 1:[1,2,3,4] -> [1,2,3,5]
        # Case 2: [9,9,9] -> [1,0,0,0]
        digits = digits[::-1]
        one, i = 1, 0

        while one:
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    one = 0
            else:
                break
            i += 1
        if one:
            digits.append(1)
        return digits[::-1]