class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurrences = {}

        for i in arr:
            occurrences[i] = occurrences.get(i, 0) + 1
        
        return len(set(occurrences.values())) == len(occurrences)