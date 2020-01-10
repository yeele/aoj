# https://www.pramp.com/challenge/15oxrQx6LjtQj9JK9XlA

def find_duplicates(arr1, arr2):
    i = j = 0
    ans = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            ans.append(arr1[i])
            j += 1
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1
    return ans

arr1 = [1, 2, 3, 5, 6, 7]
arr2 = [3, 6, 7, 8, 20]
print(find_duplicates(arr1, arr2))


# intervewers solution, which uses extra spaces...
def find_duplicates1(arr1, arr2):
    unique_numbers = set()
    result = []
    for num in arr1:
        unique_numbers.add(num)
    for num in arr2:
        if num in unique_numbers:
            result.append(num)
    return result









def right_index(S):

    def rec(S, i, j):
        piv = i + ((j-i)//2)

    return -1


S = [-8, 0, 2, 5]

print(right_index(S))