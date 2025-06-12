def sum(nums):
  # Check that we only have numbers
  for num in nums:
     try:
         if "" + num:
             return False    
     except TypeError:
         continue

    # Now that we know we have numbers, let's perform the calculation
    total = 0
    for num in nums:
        total += num

    return total
    
numbers=[2,3,4,5]
mixed=[2,"hello",3,4,5]
print(sum(numbers))
print(sum(mixed))
