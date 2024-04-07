# Function to return area of rectangle given length and width:
def rect_area(length, width):
    return length * width

length = int(input("Enter an integer for length: "))
width = int(input("Enter an integer for width: "))

result = rect_area(length, width)
print(f"Area = {result}")