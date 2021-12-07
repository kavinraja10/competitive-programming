    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a=Counter(ransomNote)
        b=Counter(magazine)
        for i in ransomNote:
            if i not in magazine or  a[i]>b[i]:
                return 0
        return 1
