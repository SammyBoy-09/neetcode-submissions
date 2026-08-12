class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_map = defaultdict(list)

        for i in strs:
            k = tuple(sorted(i))

            ana_map[k].append(i)

        return list(ana_map.values())