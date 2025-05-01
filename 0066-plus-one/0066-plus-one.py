class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        max_index = len(digits)-1
        min_index = 0

        for i in range(max_index, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                break
            else:
                digits[i] = 0
                if i == min_index:
                    digits.insert(0, 1)
                    break
        return digits