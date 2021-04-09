def get_mid(l):
    """快慢指针"""
    if not l.head.next:
        return -1

    s = q = l.head
    while(q and q.next):
        s = s.next
        q = q.next.next

    return s.data

