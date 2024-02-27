total_height = 0
heights = input("Enter heights of students ").split()

for n in range (0, len(heights)):
    heights[n] = int(heights[n])

for height in heights:
    total_height += height
print(f"Number of students: {len(heights)}")
print(f"Total height: {total_height}")
average = total_height / len(heights)
print(f"Average height: {average}")