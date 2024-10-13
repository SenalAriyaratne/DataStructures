from doubly_linked_list import DoublyLinkedList

dll = DoublyLinkedList(4)

dll.insert_at_front(1)
dll.insert_at_front(2)
dll.insert_at_front(3)

print(dll)
print(f"Head is  {dll.check_head()}")
print(f"Tail is  {dll.check_tail()}")