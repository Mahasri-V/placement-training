numbers = [1, 3, 3, 6, 7, 8, 9]
sorted_numbers = sorted(numbers)
n = len(sorted_numbers)
median = (sorted_numbers[n//2] if n % 2 != 0
          else (sorted_numbers[n//2 - 1] + sorted_numbers[n//2]) / 2)
print("Median:", median)
