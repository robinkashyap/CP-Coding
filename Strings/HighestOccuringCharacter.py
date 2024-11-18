# Time Complexity - O(n)
# Space Complexity - O(1)

# For a given a string(str), find and return the highest occurring character.
# If there are two characters in the input string with the same frequency, return the character which comes first.


def highestOccuringChar(str):
    n = len(str) 
    arr = [0]*26
    for i in str:
        i = i.lower()
        arr[ord(i)-97] += 1
    max = 0
    for j in str:
        if arr[ord(j)-97]>max:
            max = arr[ord(j)-97]
            k = j
    return k, max

str = 'xabbaab'
char,occurance = highestOccuringChar(str)
print(f"'{char}' occured {occurance} times in the string")
