# Homework: Your job is to make a custom calculator. 
# Your calculator should accept at least three values. 

# For example height, width, length

# It should print a prompt that makes it clear what 
# is being calculated. 

# For example: 
# Enter height, width, and length to calculate the area of a cube
# Height: 3
# Width: 4
# Length: 2

# After accepting input the calculator should perform 
# an accurate calculation and display the results in 
# a clear and well formatted message. 

# For example: A cube with a height of 3, width of 4, and length of 2 has an area of 
# You can accept string input that becomes part of the descirption. 
# For example: Input units: inches

# Be sure to convert your numeric values to numbers before performing math operations!

print("Enter your height and find out how many apples tall you are: ")
feet = float(input("Feet w/o inches: "))
feet = feet * 12
inches = float(input("Inches: "))


def apples():
    height_in = float(feet + inches) / 4
    return height_in
print(f"You are approximately {apples()} apples tall!")

#I thought this calculator was a cute idea because Hello Kitty's height is measured in apples!