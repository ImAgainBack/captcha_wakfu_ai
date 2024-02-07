data=int(['4', '7', '5', '6', '8', '2', '3', '1', '4', '7', '5', '6', '8', '2', '3', '1', '4', '7', '5', '6', '8', '2', '3', '1', '4', '7', '5', '6', '8', '2', '3', '1', '4', '7', '5', '6', '8', '2', '3', '1', '4', '7', '5', '6', '8', '2', '3', '1', '4', '7', '5', '6', '8', '2', '3', '1', '4', '7', '5', '6', '8', '2', '3', '1', '4', '7', '5', '6', '8', '2', '3', '1', '4', '7', '5', '6', '8', '2', '3', '1'])

def top_three_numbers(nums):
    count = {}
    # Count occurrences of each number
    for num in nums:
        count[num] = count.get(num, 0) + 1
    
    # Sort the dictionary by values in descending order
    sorted_count = sorted(count.items(), key=lambda x: x[1], reverse=True)
    
    # Get the three most common numbers
    top_three = [x[0] for x in sorted_count[:3]]
    return top_three

# Example list of integers
nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
print(top_three_numbers(data))  # Output: [5, 4, 3]
