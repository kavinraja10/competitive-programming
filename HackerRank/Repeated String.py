def repeatedString(s, n):
    # Write your code here
    c=s.count('a')
    a=n//len(s)
    if len(s)%n==0:
        return c*a
    else:
        return (s[:n%len(s)].count('a'))+(c*a)
