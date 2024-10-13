class Node:
    def __init__(self, data: any):
        self._data = data
        self._nxt = None
        self._prev = None
    
    def get_data(self) -> any:
        return self._data
    
    def set_data(self, new_value: any):
        self._data = new_value
    
    def set_node(self, node: 'Node', node_type: str):
        if node_type == "nxt":
            self._nxt = node
        elif node_type == "prev":
            self._prev = node
        else:
            print(f"Invalid node type {node_type}, it must be either nxt or prev")
    def get_next(self):
        return self._nxt
    
    def get_previous(self):
        return self._prev