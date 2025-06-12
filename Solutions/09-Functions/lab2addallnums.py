def sum(nums):
    """
    Will calculate all numbers in a mixed list, but not the strings.
    """

    # Set the total as a real number
    total = 0
    # Loop through all elements in the list
    for num in nums:
        try:
            # Try to add numbers.  This will fail if num is a string
            total += num
        except TypeError:
            # If num is a string, let's try to convert it to see if it is a number string
            try:
                # Add the converted string to a number and add
                total += float(num)
            except ValueError:
                # The string was not a number so get the next value from the list
                continue

    # Return the total of all numbers in the list added together
    return total
    
numbers=[2,3,4,5]
mixed=[2,"hello",3,4,"Bad",5,6,"42.1"]
print(sum(numbers))
print(sum(mixed))
