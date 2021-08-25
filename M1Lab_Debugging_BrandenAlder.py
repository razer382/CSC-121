# Debugging assignment to align information correctly
# 8/25/2021
# CSC121 M1Lab– Debugging
# Branden Alder

print('number\t square\t cube')
for x in range(0,6,1): # For loop going from 0 to 5
    print(f'{x : > 6}  {x ** 2 : > 7}{x ** 3 : > 6}') # Uses fstring to to align numbers to the correct place

