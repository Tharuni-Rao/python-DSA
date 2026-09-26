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