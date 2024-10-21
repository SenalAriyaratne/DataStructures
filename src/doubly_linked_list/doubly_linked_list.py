from node import Node
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DoublyLinkedList:
    def __init__(self, size: int):
        self._size = size - 1
        self._count = 0
        self._head = None
        self._tail = None
        self._logger = logger
    
    def insert_at_front(self, data: any):
        new_node = Node(data)
        if self._count == 0 and self._head is None:
            self._add_first_element(new_node)
        else:
            if self._has_space:
                self._set_head(new_node)
            else:
                self._logger.warning("Not enough space")

    
    def insert_at_back(self, data:any):
        new_node = Node(data)
        if self._count == 0 and self._head is None:
            self._add_first_element(new_node)
        else:
            if self._has_space():
                self._set_tail(new_node)
                self._logger.info(f"Added new element to the back, the new tail is  {self._tail}")
            else:
                self._logger.error("Not enough space")
    
    def insert_at(self, data:any, pos:any):

        # check if pos is closer to head or tail
        if pos >= self._size or pos > self._count:
            self._logger.error(f"Invalid postion")
            return
        new_node = Node(data)

        if pos == 0:
            self.insert_at_front(data)
            return
        
        if pos == self._count:
            self.insert_at_back(data)
            return

        mid = int(self._count / 2)
       
        if pos > mid:
            #traverse from tail
            idx = self._count - 1
            current = self._tail
            while current:
                if idx == pos - 1:
                    self._link_nodes(pos, new_node, current)
                    break
                else:
                    idx -= 1
                    current = current.get_previous()
        else:
            idx = 0
            current = self._head
            while current:
                
                if idx == pos - 1:
                    self._link_nodes(pos, new_node, current)
                    break
                else:
                    idx += 1
                    current = current.get_next()
    
    def delete_at_front(self):
        if self._is_empty():
            self._logger.warning("Empty list, nothing to remove")
            return
        old_head = self._head
        self._head = old_head.get_next()
        self._head.set_node(None, "prev")
        self._count -= 1
        self._logger.info(f"Successfully removed {old_head}, new head of the list is {self._head}")

    def delete_at_back(self):
        if self._is_empty():
            self._logger.warning("Empty list, nothing to remove")
            return
        old_tail = self._tail
        self._tail = old_tail.get_previous()
        self._tail.set_node(None, "nxt")
        self._count -= 1
        self._logger.info(f"Successfully removed{old_tail}, new tail of the list is {self._tail}")

    def delete_at(self, pos:int):
        if self._is_empty():
            self._logger.warning("Empty list, nothing to remove")
            return
        if pos >= self._size or pos > self._count:
            self._logger.error(f"Invalid postion")
            return
        if pos == 0:
            self.delete_at_front()
            return
        if pos == self._count:
            self.delete_at_back()
            return

        mid = int(self._count / 2)

        if pos > mid:
            idx = self._count - 1
            current = self._tail

            while current:
                if idx == pos -1:
                    self._link_after_remove(current)
                    break
                else:
                    idx -= 1
                    current = current.get_previous()
        else:
            idx = 0
            current = self._head
            while current:
                if idx == pos - 1:
                    self._link_after_remove(current=current)
                    break
                else:
                    idx += 1
                    current = current.get_next()

    def _link_after_remove(self, current):
        current_prev = current.get_previous()
        current_nxt = current.get_next()
        current_prev.set_node(current_nxt, "nxt")
        current_nxt.set_node(current_prev, "prev")
        self._count -= 1
        self._logger.info(f"Successfully removed the node {current}")

    def check_head(self):
        return self._head.get_data()
    
    def check_tail(self):
        return self._tail.get_data()

    def _is_empty(self):
        return self._count == 0
    
    def _add_first_element(self, new_node: Node):
        self._head = new_node
        self._tail = new_node
        self._count += 1
        self._logger.info(f"Added new element, the current head is {self._head} and tail is pointing to {self._tail}")

    def _set_tail(self, new_node: Node):
        try:
            old_tail = self._tail
            self._tail.set_node(new_node,"nxt")
            self._tail = new_node
            self._tail.set_node(old_tail, "prev")
            self._count += 1
        except AttributeError as err:
            self._logger.error(err)
        except Exception as exerr:
            self._logger.error(f"An unexpected error occured: {exerr}")
           
    def _link_nodes(self, pos, new_node, current):
        current_next = current.get_next()
        current_prev = current.get_previous()
        new_node.set_node(current, "nxt")
        new_node.set_node(current_prev, "prev")
        current.set_node(new_node, "prev")
        current_prev.set_node(new_node, "nxt")
        self._count += 1
        self._logger.info(f"Added a new node {new_node} at position {pos}")

    def _set_head(self, new_node):
        old_head = self._head
        self._head.set_node(new_node,"prev")
        self._head = new_node
        self._head.set_node(old_head,"nxt")
        self._count += 1
        self._logger.info(f"Added new element, the current head is {self._head}")
    
    def _has_space(self) -> bool:
        return self._count < self._size
    
    def __str__(self):
        values = []
        current = self._head

        while current:
            values.append(str(current.get_data()))
            current = current.get_next()
        return "<->".join(values)