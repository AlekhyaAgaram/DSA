class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        
        # 1. Store last seen index of each digit
        last_seen = {}
        for i in range(len(digits)):
            last_seen[int(digits[i])] = i

        # 2. Find the first digit that can be swapped with a larger one
        for i in range(len(digits)):
            curr = int(digits[i])
            for big in range(9, curr, -1):
                # Check that 'big' actually exists and appears after position i
                if big in last_seen and last_seen[big] > i:
                    j = last_seen[big]
                    digits[i], digits[j] = digits[j], digits[i]
                    return int("".join(digits))

        return num