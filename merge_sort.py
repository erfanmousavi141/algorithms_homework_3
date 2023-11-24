#!/usr/bin/python


def merge(left_half, right_half) -> list:
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

    merged += left_half[left_index:]
    merged += right_half[right_index:]
    return merged


def merge_sort(lst: list) -> list:
    lstLen = len(lst)
    if lstLen <= 1:
        return lst
    mid = lstLen // 2
    lefts = lst[:mid]
    rights = lst[mid:]
    return merge(merge_sort(lefts), merge_sort(rights))


array = [23, 43, 5, 4, 3, 2, 26, 8, 65, 43, 77, 93]
sorted_array = merge_sort(array)

print(sorted_array)
