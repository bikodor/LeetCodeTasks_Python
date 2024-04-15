
s = "abcdabvcd"

def solution (s):
        p = ''
        count = 0
        for i in s:
            if i in p:
                if count:
                    count = max(len(p), count)
                    parts = p.split(i, 1)
                    p = parts[1]
                    p += i
                else:
                    count = len(p)
                    parts = p.split(i, 1)
                    p = parts[1]
                    p += i
            else:
                p += i
        return max(len(p), count)

count = solution(s)

print(count)

