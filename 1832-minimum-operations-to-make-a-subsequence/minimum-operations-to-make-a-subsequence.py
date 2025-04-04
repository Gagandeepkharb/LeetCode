import bisect

class Solution:
    def minOperations(self, target: list[int], arr: list[int]) -> int:
        pos = {num: i for i, num in enumerate(target)}
        index_seq = [pos[num] for num in arr if num in pos]
        
        lis = []
        for idx in index_seq:
            insert_pos = bisect.bisect_left(lis, idx)
            if insert_pos == len(lis):
                lis.append(idx)
            else:
                lis[insert_pos] = idx
                
        return len(target) - len(lis)
