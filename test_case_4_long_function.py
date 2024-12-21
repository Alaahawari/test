# Long Function Example
def calculate_statistics(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    variance = sum((x - average) ** 2 for x in numbers) / len(numbers)
    print("Total:", total)
    print("Average:", average)
    print("Maximum:", maximum)
    print("Minimum:", minimum)
    print("Variance:", variance)
