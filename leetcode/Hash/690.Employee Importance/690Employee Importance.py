"""
# Employee info
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees: List['Employee'], idd: int) -> int:
        # 简单的图遍历
        self.es = {}
        for e in employees:
            self.es[e.id] = e
        return self.dfs(idd)  
            
    def dfs(self, idd):
        e = self.es[idd]
        sumn = e.importance
        for sub_idd in e.subordinates:
            sumn += self.dfs(sub_idd)
        return sumn
        