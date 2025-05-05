def reverse_number(num):
    reversed_num = 0
    while num > 0:
        digit = num % 10               
        reversed_num = reversed_num * 10 + digit  
        num = num // 10        
    return reversed_num        

print(reverse_number(1234))   # Output: 4321
print(reverse_number(1000))   # Output: 1
