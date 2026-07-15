
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
        against_map[a] = b
        against_map[b] = a

    path = set()
    max_sum = 0
    results = set()

    def dfs(current_sum: int):
        nonlocal max_sum, results, path

        if current_sum > max_sum:
            max_sum = current_sum  # wei chu li shegnxu bianhao
            results = set(path)

            # 这里不能return，避免局部最优解

        if len(path) == k:
            return

        for type_, node in have_map.items():
            # 这里用了 type_ not in path 来避免 重复添加进 path
            if against_map.get(type_, "noway") not in path and type_ not in path:
                path.add(type_)

                dfs(current_sum + node[0])

                path.pop()

    dfs(0)

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
