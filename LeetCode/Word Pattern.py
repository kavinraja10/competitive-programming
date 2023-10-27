def wordPattern(self,pattern: str, s: str) -> bool:
    s = list(map(str,s.split()))
    if len(pattern) != len(s):
        return (False)
    if len(set(pattern)) != len(set(s)):
        return (False)
    d=dict()

    for i in range(len(pattern)):
        if pattern[i] not in d:
            d[pattern[i]] = s[i]
        elif d[pattern[i]] != s[i]:
            return False
    return True
