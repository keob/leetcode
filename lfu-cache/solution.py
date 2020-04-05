class DLinkedListNode:
    def __init__(self, key=None, value=None, frequency=None):
        self.key = key
        self.value = value
        self.freq = frequency
        self.pre = None
        self.nxt = None

    def __repr__(self):
        return "k:{}, v{}, f:{}".format(self.key, self.value, self.freq)


def get_dlinkedlist():
    head = DLinkedListNode()
    tail = DLinkedListNode()
    head.nxt = tail
    tail.pre = head
    return head, tail


class LFUCache:
    def __init__(self, capacity: int):
        import collections
        self.capacity = capacity
        self.size = 0
        self.freq_map = collections.defaultdict(get_dlinkedlist)
        self.key_map = {}
        self.min_freq = 0

    def _add_node(self, node):
        freq = node.freq
        head = self.freq_map[freq][0]
        node.nxt = head.nxt
        node.pre = head
        head.nxt = node
        node.nxt.pre = node

    def _del(self, freq):
        node = self.freq_map[freq][1].pre
        self._remove(node)
        self.key_map.pop(node.key)

    def _remove(self, node):
        pre_node = node.pre
        nxt_node = node.nxt
        freq = node.freq
        if self.freq_map[freq] == (pre_node, nxt_node):
            self.freq_map.pop(freq)
        else:
            pre_node.nxt = nxt_node
            nxt_node.pre = pre_node

    def _update_node(self, node, val):
        self._remove(node)
        if node.freq == self.min_freq and node.freq not in self.freq_map:
            self.min_freq += 1
        node.freq += 1
        node.value = val
        self._add_node(node)

    def get(self, key: int) -> int:
        node = self.key_map.get(key, None)
        if node is None:
            return -1
        else:
            self._update_node(node, node.value)
            return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return None
        if key in self.key_map:
            node = self.key_map[key]
            self._update_node(node, value)
        else:
            node = DLinkedListNode(key, value, 1)
            if self.size == self.capacity:
                self._del(self.min_freq)
                self.size -= 1
            self.min_freq = 1
            self._add_node(node)
            self.key_map[key] = node
            self.size += 1

