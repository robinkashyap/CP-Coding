# Time Complexity - O(n)
# Space Complexity - O(1) as arr is of fixed size

# For a given two strings, 'str1' and 'str2', check whether they are a permutation of each other or not.
# Two strings are said to be a permutation of each other when either of the string's characters can be\n
# rearranged so that it becomes identical to the other one.


def permutation(str1, str2):
    if len(str1) != len(str2):
        return False
    else:
       arr = [0]*26
       for i in str1:
           i = i.lower()
           arr[ord(i)-97] = arr[ord(i)-97] + 1
       for j in str2:
           j = j.lower()
           arr[ord(j)-97] = arr[ord(j)-97] - 1
       for i in range(len(arr)):
           if arr[i] != 0:
               return False
       return True

print(permutation('string', 'srting'))