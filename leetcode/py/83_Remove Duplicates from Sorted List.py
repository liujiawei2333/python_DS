def deleteDuplicates1(head):
    if head == None or head.next== None:#零结点和一个结点的情况
        return head        
    p = head
    while True:
        if p.val == p.next.val:
            p.next = p.next.next#跳过值相同的结点
        else:
            p = p.next
        if p.next==None:#尾结点
            break

    return head