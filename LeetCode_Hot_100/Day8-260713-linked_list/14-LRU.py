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
        self.key_map: dict[int, ListNode] = {}

        self.head = ListNode(0, 0)
        self.tail = ListNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.key_map:
            return -1

        current_node: ListNode = self.key_map[key]

        self._up(current_node)

        return current_node.value

        # 最久未使用的关键字
        # 这里使用了 要翻新

    def put(self, key: int, value: int) -> None:

        if key in self.key_map:
            current_node = self.key_map[key]
            current_node.value = value

            self._up(current_node)

            # 若有则更新
            # 若没有则加入，若满 则 last used 出

            # 新进的翻新
        else:
            current_node = ListNode(key, value)

            self.key_map[key] = current_node

            # 新进放前面

            current_node.next = self.head.next
            current_node.prev = self.head

            current_node.next.prev = current_node
            current_node.prev.next = current_node

            if len(self.key_map) > self.capacity:
                to_remove_node: ListNode = self.tail.prev

                # 前后连上
                to_remove_node.prev.next = to_remove_node.next
                to_remove_node.next.prev = to_remove_node.prev

                # 删 last recently used
                del self.key_map[to_remove_node.key]

    def _up(self, target_node: ListNode):

        # 只有 已存在 才需要 Up

        # 已存在，则 前后连上，自己剥离
        target_node.next.prev = target_node.prev
        target_node.prev.next = target_node.next

        # 自己前变head，后接之前second
        target_node.next = self.head.next
        target_node.prev = self.head

        target_node.prev.next = target_node
        target_node.next.prev = target_node
