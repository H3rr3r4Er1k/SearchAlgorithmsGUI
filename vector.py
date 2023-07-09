def quicksort(vector):
    if len(vector) <= 1:
        return vector
    pivot = vector[len(vector) // 2]
    left = [x for x in vector if x < pivot]
    middle = [x for x in vector if x == pivot]
    right = [x for x in vector if x > pivot]
    return quicksort(left) + middle + quicksort(right)
