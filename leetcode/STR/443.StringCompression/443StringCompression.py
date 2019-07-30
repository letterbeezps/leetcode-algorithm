class Solution:
    def compress(self, chars: List[str]) -> int:
        anchor, write = 0, 0
        for read, c in enumerate(chars):
            if read + 1 == len(chars) or chars[read + 1] != c:
                chars[write] = chars[anchor]
                write += 1
                if read > anchor:
                    for i in str(read-anchor+1):  # look example 3
                        chars[write] = i
                        write += 1
                
                anchor = read+1
        return write