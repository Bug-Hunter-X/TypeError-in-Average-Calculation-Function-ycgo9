def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    return sum(numbers) / len(numbers)

# Example usage with potential error
data = [1, 2, 3, 4, 5, 'a']
average = calculate_average(data)
print(f"The average is: {average}")

# Example usage with no error
data2 = [1, 2, 3, 4, 5]
average2 = calculate_average(data2)
print(f"The average is: {average2}")