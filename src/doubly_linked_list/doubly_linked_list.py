from node import Node
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DoublyLinkedList:
    def __init__(self, size: int):
        self._size = size
        self._count = 0
        self._head = None
        self._tail = None
        self._logger = logger

    def insert_at_front(self, data: any):
        new_node = Node(data)
        if self._count == 0 and self._head is None:
            self._head = new_node
            self._tail = new_node
            self._count += 1
            self._logger.info(f"Added new element, the current head is {self._head}")
        else:
            if self._has_space:
                self._set_head(new_node)
            else:
                print(f"Not enough space...")
    
    def insert_at_back(self, data:any):
        if self._count == 0 and self._head is None:
            print(f"List is empty, Add an element at front")
            return
        else:
            pass
            

    def insert_at(self, data:any, pos:any):
        pass
    
    def check_head(self):
        return self._head.get_data()
    
    def check_tail(self):
        return self._tail.get_data()

    def _set_head(self, new_node):
        old_head = self._head
        self._head.set_node(new_node,"prev")
        self._head = new_node
        self._head.set_node(old_head,"nxt")
        self._count += 1
    
    def _has_space(self) -> bool:
        return self._count < self._size
    
   
    def __str__(self):
        values = []
        current = self._head

        while current:
            values.append(str(current.get_data()))
            current = current.get_next()
        return "<->".join(values)