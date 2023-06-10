from app import html_content
import statistics
from collections import Counter
import random

colors = html_content()

# Convert colors to lowercase and split into individual colors
lowercase_colors = [color.lower() for color in colors]

individual_colors = [color.strip() for color in ",".join(lowercase_colors).split(",")]

#   one
def calculate_mean_color():
    # Calculate the mean color
    mean_color = statistics.mode(individual_colors)

    print(f"The mean color of shirts is: {mean_color}")


calculate_mean_color()

#   two
def calculate_most_worn_color():
    # Count the frequency of each color
    mostly_worn_color = Counter(individual_colors)

    # Get the color with the highest frequency
    most_common_color = mostly_worn_color.most_common(1)[0][0]

    print(f"The color mostly worn throughout the week is: {most_common_color}")


calculate_most_worn_color()

#   three
def calculate_median_color():
    # Sort the individual colors
    sorted_colors = sorted(individual_colors)

    # Find the median color
    median_index = len(sorted_colors) // 2
    median_color = sorted_colors[median_index]

    print(f"The median color of shirts is: {median_color}")


calculate_median_color()

#   four
# Calculate the variance of the colors
# variance = statistics.variance(individual_colors)

# print(f"The variance of the colors is: {variance}")

#   five
def probability_of_red():
    # Count the frequency of each color
    color_frequency = Counter(individual_colors)

    # Get the frequency of red
    red_frequency = color_frequency["red"]

    # Calculate the probability of choosing red
    total_colors = len(individual_colors)
    probability_red = red_frequency / total_colors

    print(f"The probability of choosing red is: {probability_red}")


probability_of_red()

#  seven
def recursive_search(numbers, target):
    if not numbers:
        return False
    elif numbers[0] == target:
        return True
    else:
        return recursive_search(numbers[1:], target)


# Example usage
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_number = int(input("Enter a number to search for: "))

if recursive_search(number_list, target_number):
    print(f"The number {target_number} is found in the list.")
else:
    print(f"The number {target_number} is not found in the list.")

#   eight
def generate_random():
    # Generate a random 4-digit number of 0s and 1s
    random_number = "".join(random.choices(["0", "1"], k=4))

    # Convert the random number to base 10
    base_10_number = int(random_number, 2)

    print(f"The random number {random_number} in base 10 is: {base_10_number}")


generate_random()

#   nine
def fibonacci_sum(n):
    fib_sequence = [0, 1]

    for i in range(2, n):
        fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])
    return sum(fib_sequence)


# Calculate the sum of the first 50 Fibonacci numbers
sum_of_fibonacci = fibonacci_sum(50)

print(f"The sum of the first 50 Fibonacci numbers is: {sum_of_fibonacci}")
