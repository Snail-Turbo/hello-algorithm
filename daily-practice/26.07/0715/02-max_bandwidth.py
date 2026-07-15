
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
        against_map[a] = against_map.get(a, []) + [b]
        against_map[b] = against_map.get(b, []) + [a]

    path = set()
    max_sum = 0
    results = set()

    type_keys = list(have_map.keys())

    def dfs(index, current_sum: int):
        nonlocal max_sum, results, path

        if current_sum > max_sum:
            max_sum = current_sum  # 未处理 相等时按字典序选更小的
            results = set(path)

            # 这里不能return，避免局部最优解

        if len(path) == k:
            return

        for i in range(index, len(type_keys)):
            cur_type = type_keys[i]
            cur_price = have_map[cur_type][0]
            antagonists = against_map.get(cur_type, [])

            if not (set(antagonists) & path):  # 没有交集，则没有冲突
                path.add(cur_type)

                dfs(i + 1, current_sum + cur_price)

                path.remove(cur_type)

    dfs(0, 0)

    print(max_sum)
    results = [have_map[type__][1] for type__ in list(results)]
    results.sort()

    print(results[0])
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
