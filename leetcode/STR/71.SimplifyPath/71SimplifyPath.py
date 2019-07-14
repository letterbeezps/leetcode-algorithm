class Solution:
    def simplifyPath(self, path: str) -> str:
        path += '/'
        res, s = [], ''
        for x in path:
            if not res:
                res.append(x)
            elif x != '/':
                s += x
            else:
                if s == '..':
                    if len(res) > 1: 
                        # 判断根目录
                        res.pop()
                        while res[-1] != '/':
                            res.pop()
                elif s != '.' and s != '':
                    res.append(s)
                    res.append('/')
                s = ''
                
        if len(res) > 1:
            res.pop()
        return ''.join(res)
                    
