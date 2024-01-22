def qvucl_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
    less = [ i for i in array[1 :] if i <= pivot  ]
    reater =  [ i for i in array[1 :] if i > pivot ]
    return qvucl_sort(less) + [pivot] + qvucl_sort(reater)
print(qvucl_sort([2,5,45,34,7,9,87,5,7,34,]))