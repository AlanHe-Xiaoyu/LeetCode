class LRUCache:
    """
    Soln - Double LinkedList (append @tail, pop @head)
    Runtime: 212 ms, faster than 70.54% of Python3 online submissions for LRU Cache.
    Memory Usage: 23.3 MB, less than 27.03% of Python3 online submissions for LRU Cache.
    """
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        # Sentinel nodes
        self.head = DLL(None, None)
        self.tail = DLL(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        node = self.cache.get(key)
        if node is None:
            return -1
        self.delete_node(node)
        self.add_node(node)
        return node.v

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)
        if node is None:
            if len(self.cache) == self.capacity:
                old_node = self.cache.pop(self.head.next.k)
                self.delete_node(old_node)
        else:
            self.delete_node(node)
        
        new_node = DLL(key, value)
        self.cache[key] = new_node
        self.add_node(new_node)
        
    def delete_node(self, node):
        k = node.k
        node.next.prev = node.prev
        node.prev.next = node.next
        
    def add_node(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
        
        

class DLL:
    def __init__(self, k, v):
        self.k = k
        self.v = v
        self.next = None
        self.prev = None

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)