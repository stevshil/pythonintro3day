def sum(nums):
    # Set our total variable so that it is a true number
    total = 0
    # Loop through all the values
    for num in nums:
        try:
            # Check if we have a real number
            if "" + num:
                # Exit the function if we have a string
                return False    
        except TypeError:
            # If ""+num generated an exception then we have a true number, so add it to total
            total += num

    # Return the final total back to the main program
    return total
    
numbers=[2,3,4,5]
mixed=[2,"hello",3,4,5]
print(sum(numbers))
print(sum(mixed))
