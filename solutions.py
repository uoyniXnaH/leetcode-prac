class Solution:    
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        min = nums[0]
        for number in nums:
            if number < min:
                min = number
        min = abs(min) if min < 0 else 0
        nums_offset = [number + min for number in nums]
        target_offset = target + 2*min
        target_offset_half = target_offset / 2
        if nums_offset.count(target_offset_half) >= 2:
            index1 = nums_offset.index(target_offset_half)
            index2 = nums_offset.index(target_offset_half, index1+1)
            return [index1, index2]
        nums_lt_half = [number for number in nums_offset if number < target_offset_half]
        if len(nums_lt_half) == 0:
            return [0, 1]
        nums_ge_half = [number for number in nums_offset if number >= target_offset_half]
        diff_lt_half = [target_offset_half - number for number in nums_lt_half]
        diff_ge_half = [number - target_offset_half for number in nums_ge_half]
        diff_merge = diff_lt_half + diff_ge_half
        diff_merge_sorted = sorted(diff_merge)
        result_diff_candidates = []
        for i in range(len(diff_merge_sorted)-1):
            if diff_merge_sorted[i] == diff_merge_sorted[i+1]:
                result_diff_candidates.append(diff_merge_sorted[i])
        for candidate in result_diff_candidates:
            if candidate in diff_lt_half and candidate in diff_ge_half:
                index1 = nums_offset.index(target_offset_half - candidate)
                index2 = nums_offset.index(target_offset_half + candidate)
                return [index1, index2]
            
    def isPalindrome(self, x: int) -> bool:
        x_str = f"{x}"
        rts_x = x_str[::-1]
        return x_str == rts_x