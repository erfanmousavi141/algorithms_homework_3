#!/usr/bin/python

def merge(left_half: list, right_half: list) -> list:
    merged = []
    left_index = 0
    right_index = 0
    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index] <= right_half[right_index]:
            merged.append(left_half[left_index])
            left_index += 1
        else:
            merged.append(right_half[right_index])
            right_index += 1
    merged.extend(right_half[right_index:])
    merged.extend(left_half[left_index:])
    return merged


def merge_sort(arr: list) -> list:
    lstLen = len(arr)
    if lstLen <= 1:
        return arr
    mid = lstLen // 2
    lefts = arr[:mid]
    rights = arr[mid:]
    return merge(merge_sort(lefts), merge_sort(rights))


array = [23, 43, 5, 4, 3, 2, 26, 8, 65, 93, 43]
sorted_array = merge_sort(array)
print(sorted_array)
