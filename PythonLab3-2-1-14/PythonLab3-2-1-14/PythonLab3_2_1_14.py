# 3.2.1.14 LAB: Essentials of the while loop
# 
# [1]           ;; When building a pyramid it is important to remember you start
# [2][3]        ;; at the bottom and build one layer at a time.
# [4][5][6]     ;; However due to how the output is displayed we end up with the
# [7][8][9][10] ;; example on the left - a pyramid 'built' on its side.
# 
# Prompts the user to enter an integer
blocks = int(input("Enter the number of blocks: "))
height = 0
layers = 1
square = "[]"
while layers <= blocks:
    # Addition Assignment (+=) adds the value (1) with the 'height' variable's value and assigns the new value back to the 'height' variable.
    height += 1
    # Subtraction Assignment (-=) subtracts a value ('layers') from the 'blocks' variable and assigns the result back to the 'blocks' variable.
    # For every iteration we are "taking" blocks from 'blocks' and placing them in 'layers' created.
    blocks -= layers
    # Addition Assignment (+=) adds the value (1) with the 'layers' variable's value and assigns the new value back to the 'layers' variable.
    layers += 1
    # Outputs a block per user input
    print(square * height)

# Outputs any remaining blocks
print(square * blocks)
# Outputs the pyramids height
print("The height of the pyramid:", height, "\n")
