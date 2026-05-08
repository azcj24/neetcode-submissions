class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for word in strs:
            label = "".join(sorted(word))
            if label not in group:
                group[label] = []
            group[label].append(word)

        return list(group.values())