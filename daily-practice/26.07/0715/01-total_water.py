
# If you need to import additional packages or classes, please import here.\

# 非占格接水


def func():
    count = int(input())
    heights = list(map(int, input().strip().split()))

    # tmp_input_n = 5
    # tmp_input_heights = [1, 2, 3, 4, 5]
    # heights = tmp_input_heights

    heights = [0] + heights + [0]

    left, right = 0, len(heights) - 1

    left_max, right_max = 0, 0

    count = 0

    while left < right:
        if heights[left] < heights[right]:
            if heights[left] > left_max:
                left_max = heights[left]

            count += left_max
            left += 1

        else:
            if heights[right] > right_max:
                right_max = heights[right]

            count += right_max
            right -= 1

    print(count)


if __name__ == "__main__":

    func()
