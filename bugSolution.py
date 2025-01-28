def calculate_average(numbers):
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0
    return sum(numeric_numbers) / len(numeric_numbers)

# Example usage with error handling
data = [1, 2, 3, 4, 5, 'a']
average = calculate_average(data)
print(f"The average is: {average}")

data2 = [1, 2, 3, 4, 5]
average2 = calculate_average(data2)
print(f"The average is: {average2}")

data3 = []
average3 = calculate_average(data3)
print(f"The average is: {average3}")
