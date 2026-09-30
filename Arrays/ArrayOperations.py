def insert_at(arr, index, value):
    arr.append(0)
    for i in range(len(arr) - 1, index, -1):
        arr[i] = arr[i - 1]
    arr[index] = value


def delete_at(arr, index):
    for i in range(index, len(arr) - 1):
        arr[i] = arr[i + 1]
    arr.pop()


prices = [40, 60, 25, 90]

insert_at(prices, 1, 55)
print("After insertion:", prices)

delete_at(prices, 0)
print("After deletion:", prices)




def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


marks = [56, 78, 90, 43, 67, 82, 71]

result = linear_search(marks, 67)
if result != -1:
    print("Found at index:", result)
else:
    print("Not found")



marks = [56, 78, 90, 43, 67]

for i in range(len(marks)):
    print("Index", i, "-> value:", marks[i], ", id:", id(marks[i]))





    import sys

numbers = []

for i in range(10):
    numbers.append(i)
    print("Size:", len(numbers), ", Internal bytes used:", sys.getsizeof(numbers))



marks = [
    [78, 85, 62],
    [90, 71, 88],
    [60, 95, 73]
]

rows = len(marks)
cols = len(marks[0])
total = 0

for r in range(rows):
    for c in range(cols):
        total += marks[r][c]

print("Total marks:", total)
print("Student 1, Subject 2:", marks[0][1])





def two_sum_sorted(arr, target):
    left = 0
    right = len(arr) - 1

    while left < right:
        total = arr[left] + arr[right]

        if total == target:
            return left, right
        elif total < target:
            left += 1
        else:
            right -= 1

    return -1, -1





prices = [100, 250, 400, 600, 850, 1000]
budget = 1250

left_idx, right_idx = two_sum_sorted(prices, budget)

if left_idx != -1:
    print(f"Found: {prices[left_idx]} + {prices[right_idx]} = {budget}")
else:
    print("No matching pair found.")





def max_window_sum(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        if window_sum > max_sum:
            max_sum = window_sum

    return max_sum


daily_sales = [120, 90, 150, 200, 80, 60, 175, 300]
k = 3

best = max_window_sum(daily_sales, k)
print(f"Best {k}-day total: {best}")




def build_prefix_sum(arr):
    prefix = [0] * len(arr)
    prefix[0] = arr[0]

    for i in range(1, len(arr)):
        prefix[i] = prefix[i - 1] + arr[i]

    return prefix




def range_sum(prefix, i, j):
    if i == 0:
        return prefix[j]
    return prefix[j] - prefix[i - 1]


study_hours = [2, 3, 1, 4, 2, 5, 3, 2]
prefix = build_prefix_sum(study_hours)

print("Sum from day 2 to day 5:", range_sum(prefix, 2, 5))
print("Sum from day 0 to day 3:", range_sum(prefix, 0, 3))
