from collections import defaultdict
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dic = defaultdict(int)  # 
        
        for domain in cpdomains:
            count, names = domain.split()
            count = int(count)
            list_name = names.split('.')
            for i in range(len(list_name)):
                dic['.'.join(list_name[i:])] += count
                
        return ["{} {}".format(ct, name) for name, ct in dic.items()]