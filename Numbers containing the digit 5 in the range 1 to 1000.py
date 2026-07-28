def find_numbers_with_digit(digit, start_range, end_range):
  found_numbers = []
  for num in range(start_range, end_range + 1):
    if str(digit) in str(num):
      found_numbers.append(num)
  return found_numbers

# Example usage:
# Find numbers with '5' in the range 1 to 1000
numbers_with_five = find_numbers_with_digit(5, 1, 1000)
print("Numbers containing the digit '5' in the range 1 to 1000:")
print(numbers_with_five)

# You can also use the previously generated cell `6a2192c3` if you prefer a direct script.

print("Numbers containing the digit '5' in the range 1 to 1000:")
found_numbers = []
for num in range(1, 1001):
  if '5' in str(num):
    found_numbers.append(num)

print(found_numbers)