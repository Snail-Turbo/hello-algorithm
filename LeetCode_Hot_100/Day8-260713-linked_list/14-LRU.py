import sys


class ListNode:
    __slots__ = ('key', 'value', 'prev', 'next')

    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev: ListNode = None
        self.next: ListNode = None


class LRUCache:
    def __init__(self, capacity: int):

        self.capacity = capacity
        self.key_node_map = {}  # key, ListNode

        self.head = ListNode(-1, 0)
        self.tail = ListNode(-1, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.key_node_map:
            node: ListNode = self.key_node_map[key]

            # 最久未使用的关键字
            # 这里使用了 要翻新
            self._up(node)

            return node.value

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.key_node_map:
            # 若有则更新

            # 新进的翻新
            node: ListNode = self.key_node_map[key]
            node.value = value

            self._up(node)
        else:
            # 若没有则加入，若满 则 last used 出
            node = ListNode(key, value)
            self.key_node_map[key] = node

            # 新进的翻新
            self._add_after_head(node)

            # 有新进的要判断容量
            if len(self.key_node_map) > self.capacity:
                to_remove = self.tail.prev

                # tail前面的去掉，续前后
                self.tail.prev = to_remove.prev
                to_remove.prev.next = self.tail

                # 【核心】del
                del self.key_node_map[to_remove.key]

    def _add_after_head(self, target_node: ListNode):
        target_node.next = self.head.next
        target_node.prev = self.head

        target_node.next.prev = target_node
        target_node.prev.next = target_node

    def _up(self, target_node: ListNode):
        if target_node.prev is self.head:
            return

        # 已存在，则 前后连上，自己剥离
        target_node.prev.next = target_node.next
        target_node.next.prev = target_node.prev

        # 自己前变head，后接之前second
        target_node.next = self.head.next
        target_node.prev = self.head

        target_node.next.prev = target_node
        target_node.prev.next = target_node
