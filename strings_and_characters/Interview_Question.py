# Write a program to merge 2 sorted lists without using inbuild functions
# Example:
# input:
# a = [1, 5, 6, 7, 8, 9, 10]
# b = [2, 3, 6, 8, 9, 10, 12, 16, 20, 25, 27, 32]
# # output:
# # [1, 2, 3, 5, 6, 6, 7, 8, 8, 9, 9, 10, 10, 12, 16, 20, 25, 27, 32]

# def merge_sorted_list(a,b):
#     merge_list = []
#     i, j = 0, 0
#
#     while i < len(a) and j < len(b):
#         if a[i] < b[j]:
#             merge_list.append(a[i])
#             i += 1
#         else:
#             merge_list.append(b[j])
#             j += 1
#     while i < len(a):
#         merge_list.append(a[i])
#         i += 1
#     while j < len(b):
#         merge_list.append(b[j])
#         j += 1
#     return merge_list
#
# a = [1, 5, 6, 7, 8, 9, 10]
# b = [2, 3, 6, 8, 9, 10, 12, 16, 20, 25, 27, 32, 45]
# result = merge_sorted_list(a,b)
# print(result)

def merge_sorted_list(a,b):
    merge_list = []
    i, j = 0, 0
    while i<len(a) and j<len(b):
        if a[i] < b[j]:
            merge_list.append(a[i])
            i += 1
        else:
            merge_list.append(b[j])
            j += 1
    while i<len(a):
        merge_list.append(a[i])
        i += 1
    while j<len(b):
        merge_list.append(b[j])
        j += 1
    return merge_list
a = [1, 5, 6, 7, 8, 9, 10]
b = [2, 3, 6, 8, 9, 10, 12, 16, 20, 25, 27, 32]
output = merge_sorted_list(a,b)
print(output)