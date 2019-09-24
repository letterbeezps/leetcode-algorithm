# Solution 1: Establishing two hash tables and mapping each other
# Solution 2: Establishing a hash table, so that the values of the hash table may be duplicated. if no duplication exits, return True

class Solution:
    def wordPattern(self, pattern: str, S: str) -> bool:
        STR = S.split(' ')
        if len(STR) != len(pattern):
            return False
        
        Hash1 = collections.defaultdict(str)
        # Hash2 = collections.defaultdict(str)
        
        for p, s in zip(pattern, STR):
            if not Hash1[p]:
                Hash1[p] = s
            elif Hash1[p] != s:
                return False
            # if not Hash2[s]:
            #     Hash2[s] = p
            # elif Hash2[s] != p:
            #     return False
        if len(Hash1.keys()) != len(set(Hash1.values())):
            return False
        return True