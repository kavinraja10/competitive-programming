    def getDecimalValue(self, head: ListNode) -> int:
        b=''
        cur=head
        while cur!=None:
            b+=str(cur.val)
            cur=cur.next
        print(b)
        return int(b,2)
