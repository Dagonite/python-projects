# reverse_linked_list.py

# Iteratively
def reverse_list_ite(self, head):
    node = None
    while head:
        tmp = head.next
        head.next = node
        node = head
        head = tmp
    return node

# input [1,2,3,4,5]

# node = None

# 1st loop
# tmp = head.next   # [2 -> 3 -> 4 -> 5 -> None]
# head.next = node  # None
# node = head       # [1 -> None]
# head = tmp        # [2 -> 3 -> 4 -> 5 -> None]

# 2nd loop
# tmp = head.next   # [3 -> 4 -> 5 -> None]
# head.next = node  # [1 -> None]
# node = head       # [2 -> 1 -> None]
# head = tmp        # [3 -> 4 -> 5 -> None]

# 3rd loop
# tmp = head.next   # [4 -> 5 -> None]
# head.next = node  # [2 -> 1 -> None]
# node = head       # [3 -> 2 -> 1 -> None]
# head = tmp        # [4 -> 5 -> None]s

# 4th loop
# tmp = head.next   # [5 -> None]
# head.next = node  # [3 -> 2 -> 1 -> None]
# node = head       # [4 -> 3 -> 2 -> 1 -> None]
# head = tmp        # [5 -> None]

# 5th loop
# tmp = head.next   # None
# head.next = node  # [4 -> 3 -> 2 -> 1 -> None]
# node = head       # [5 -> 4 -> 3 -> 2 -> 1 -> None]
# head = tmp        # None

# node = [5 -> 4 -> 3 -> 2 -> 1 -> None]


# Recursively
def reverse_list_rec(self, head, node=None):
    if head is None:
        return node
    tmp = head.next
    head.next = node
    return self.reverse_list_rec(tmp, head)

# input [1,2,3,4,5]

# reverse_list_rec(head, node)  # [1 -> 2 -> 3 -> 4 -> 5 -> None], None
# tmp = head.next               # [2 -> 3 -> 4 -> 5 -> None]
# head.next = node              # None
# reverse_list_rec(tmp, head)   # [2 -> 3 -> 4 -> 5 -> None], [1 -> None]

# reverse_list_rec(head, node)  # [2 -> 3 -> 4 -> 5 -> None], [1 -> None]
# tmp = head.next               # [3 -> 4 -> 5 -> None]
# head.next = node              # [1 -> None]
# reverse_list_rec(tmp, head)   # [3 -> 4 -> 5 -> None], [2 -> 1 -> None]

# reverse_list_rec(head, node)  # [3 -> 4 -> 5 -> None], [2 -> 1 -> None]
# tmp = head.next               # [4 -> 5 -> None]
# head.next = node              # [2 -> 1 -> None]
# reverse_list_rec(tmp, head)   # [4 -> 5 -> None], [3 -> 2 -> 1 -> None]

# reverse_list_rec(head, node)  # [4 -> 5 -> None], [3 -> 2 -> 1 -> None]
# tmp = head.next               # [5 -> None]
# head.next = node              # [3 -> 2 -> 1 -> None]
# reverse_list_rec(tmp, head)   # [5 -> None], [4 -> 3 -> 2 -> 1 -> None]

# reverse_list_rec(head, node)  # [5 -> None], [4 -> 3 -> 2 -> 1 -> None]
# tmp = head.next               # None
# head.next = node              # [4 -> 3 -> 2 -> 1 -> None]
# reverse_list_rec(tmp, head)   # None, [5 -> 4 -> 3 -> 2 -> 1 -> None]

# reverse_list_rec(head, node)  # None, [5 -> 4 -> 3 -> 2 -> 1 -> None]
# node                          # [5 -> 4 -> 3 -> 2 -> 1 -> None]
