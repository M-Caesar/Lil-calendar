# Merge_Sort(L)
# {
#     if |L| = 1, return L
#
#     Divide L into two roughly equal parts A of B
#
#     recursive sort A and B
#     A_sorted = Merge_Sort(A)
#     B_sorted = Merge_Sort(B)
#
#     merge lists into one
#     L_sorted = Merge(A_sorted, B_sorted)
#     return L_sorted
# }

def merge_sort(L):
    if len(L) <= 1:
        return L
    
    mid = len(L) // 2
    A = L[:mid]
    B = L[mid:]
    
    A_sorted = merge_sort(A)
    B_sorted = merge_sort(B)
    
    L_sorted = merge(A_sorted, B_sorted)
    return L_sorted

def merge(A, B):
    result = []
    i = j = 0
    
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            result.append(A[i])
            i += 1
        else:
            result.append(B[j])
            j += 1
    
    result.extend(A[i:])
    result.extend(B[j:])
    return result