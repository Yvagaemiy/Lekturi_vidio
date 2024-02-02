def marge_sort(num):
    if len(num) > 1:
        mid = len(num) //2
        left = num[: mid]
        right = num[mid :]
        marge_sort(left)
        marge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                num[k] = left[i]
                i += 1
            else:
                num[k] = right[j]
                j += 1
            k += 1
            while i < len(left):
                num[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                num[k] = right[j]
                j += 1
                k += 1  

list1 = [1,5,6,4,3,5,67,12,32,45,43,67,89,6]
marge_sort(list1)
print(list1)