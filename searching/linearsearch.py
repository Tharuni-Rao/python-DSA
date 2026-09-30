def linearsearch(a,el):
  ar=[]
  for i in range(len(a)):
    if a[i] == el:
      ar.append(i)


  if len(ar)>0:        
    return ar
  return -1  

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            right = mid - 1 # Discard right half
        else:
            left = mid + 1 # Discard left half

    return -1 # Target not found

def lower_bound(arr, target):
    left, right = 0, len(arr) - 1
    answer = len(arr)

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] >= target:
            answer = mid     # Store candidate
            right = mid - 1  # Keep looking left
        else:
            left = mid + 1

    return answer

def upper_bound(arr, target):
    left, right = 0, len(arr) - 1
    answer = len(arr)

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] > target:
            answer = mid     # Store candidate
            right = mid - 1  # Keep looking left
        else:
            left = mid + 1

    return answer


def search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid

        # Condition 1: Left half is sorted
        if nums[left] <= nums[mid]:
            # Is the target inside this sorted box?
            if nums[left] <= target < nums[mid]:
                right = mid - 1 # Yes, discard right half
            else:
                left = mid + 1  # No, discard left half

        # Condition 2: Right half is sorted
        else:
            # Is the target inside this sorted box?
            if nums[mid] < target <= nums[right]:
                left = mid + 1  # Yes, discard left half
            else:
                right = mid - 1 # No, discard right half

    return -1 # Target not found

def can_finish(piles, h, speed):
    hours = 0
    for pile in piles:
        # Integer math trick for ceiling division
        hours += (pile + speed - 1) // speed
    return hours <= h







a=[1,31,12,9,18,2,12,12]
print(linearsearch(a,12))