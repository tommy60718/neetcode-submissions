from typing import List


def reverse_list(arr: List[int]) -> List[int]:
    newList = []
    for _ in range(len(arr)):
        newList.append(arr.pop())
    return newList

# do not modify below this line
print(reverse_list([1, 2, 3]))
print(reverse_list([3, 2, 1, 4, 6, 2]))
print(reverse_list([1, 9, 7, 3, 2, 1, 4, 6, 2]))
