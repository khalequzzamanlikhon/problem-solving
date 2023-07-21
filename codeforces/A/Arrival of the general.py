def minimum_seconds_to_lineup(n, heights):
    min_height = max_height = heights[0]
    min_index = max_index = 0

    for i in range(1, n):
        a = heights[i]
        if a > max_height:
            max_height = a
            max_index = i
        if a <= min_height:
            min_height = a
            min_index = i

    distance = max_index + (n - 1 - min_index) - (1 if min_index < max_index else 0)
    return distance

# Input
n = int(input())
heights = list(map(int, input().split()))

# Calculate the minimum seconds needed to form the line-up
result = minimum_seconds_to_lineup(n, heights)

# Output the result
print(result)
