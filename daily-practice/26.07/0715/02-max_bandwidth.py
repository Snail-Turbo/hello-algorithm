
# If you need to import additional packages or classes, please import here.

def func():

    count, k = map(int, input().strip().split())

    prices = list(map(int, input().strip().split()))
    type_list = input().strip().split()

    have_map = {}
    for i in range(count):
        current_price = prices[i]
        current_type = type_list[i]

        if current_type in have_map:
            already_price = have_map[current_type][0]
            if current_price > already_price:
                have_map[current_type][0] = current_price
                have_map[current_type][1] = i
        else:
            have_map[current_type] = [prices[i], i]

    # prices = [(prices[index], index) for index in range(len(prices))]

    against_count = int(input())
    against_map = {}
    for _ in range(against_count):
        a, b = input().strip().split()
        against_map.setdefault(a, set()).add(b)
        against_map.setdefault(b, set()).add(a)

    path_indexes = []          # 存原始索引，天然有序
    path_type_set = set()   # 存类型名，O(1) 冲突检查
    max_sum = -1
    results = []     # 最优解的索引列表

    # 按最小原始索引排序，DFS 按此顺序遍历 → path 天然递增
    type_keys = sorted(have_map.keys(), key=lambda t: have_map[t][1])

    def dfs(index, current_sum: int):
        nonlocal max_sum, results, path_indexes, path_type_set

        # path 存的是索引，天然递增 → 直接比 list 就是字典序
        if current_sum > max_sum or (current_sum == max_sum and path_indexes < results):
            max_sum = current_sum
            results = path_indexes.copy()

        if len(path_indexes) == k:
            return

        for i in range(index, len(type_keys)):
            cur_type = type_keys[i]
            cur_price = have_map[cur_type][0]
            cur_idx = have_map[cur_type][1]
            antagonists = against_map.get(cur_type, set())

            if not (antagonists & path_type_set):  # 没有交集，则没有冲突
                path_indexes.append(cur_idx)               # 存索引
                path_type_set.add(cur_type)             # 存类型（冲突检查用）

                dfs(i + 1, current_sum + cur_price)

                path_indexes.pop()
                path_type_set.remove(cur_type)

    dfs(0, 0)

    print(max_sum)
    # best_path 已经是索引列表，直接输出
    results = sorted(results)

    print(results[0], end="")
    for i in range(1, len(results)):
        print(f" {results[i]}")


"""
6 2
100 200 150 300 250 180
n78 n41 n78 n28 n41 n28
1
n28 n41
"""

if __name__ == "__main__":

    func()
