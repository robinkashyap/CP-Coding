# Time Complexity - O(n)
# Auxilary Space Complexity - O(1)
# Total Space Complexity - O(n)

# Count the number of vowels, characters, digits and special character


def countVCDS(str):
    v, c, d, s = 0, 0, 0, 0
    for i in str:
        if((i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z')):
            i = i.lower()
            if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
                v = v + 1
            else:
                c = c + 1
        elif (i >= '0' and i <= '9'):
            d = d + 1
        else:
            s = s + 1
    return v, c, d, s

str = 'afIGu0&^%09'
v, c, d, s = countVCDS(str)
print(v, c, d, s)