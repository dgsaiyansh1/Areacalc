# This is a simple program that calculates the area of a rectangle

def calculate_area(length, width):
  area = length * width
  return area

# Get the dimensions of the rectangle from the user
rectangle_length = float(input("Enter the length of the rectangle: "))
rectangle_width = float(input("Enter the width of the rectangle: "))

# Calculate the area of the rectangle
rectangle_area = calculate_area(rectangle_length, rectangle_width)

# Print the result
print("The area of the rectangle is", rectangle_area)
