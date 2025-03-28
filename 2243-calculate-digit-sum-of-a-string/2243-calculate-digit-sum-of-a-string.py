class Solution:
    def digitSum(self, s: str, k: int) -> str:
        
        len_s = len(s)

        while (len_s > k):
            new_s = ''
            start_indx = 0
            end_indx = start_indx + k
            
            while (start_indx < len_s):
                group_sum = 0
                sub_str = s[start_indx : end_indx]
                group_sum = sum([int(d) for d in list(sub_str)])
                new_s += str(group_sum)
                start_indx += k
                end_indx += k
            s = new_s
            len_s = len(s)

        return s
        