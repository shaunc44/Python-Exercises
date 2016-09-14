def digits_multiply(nums):

	#Convert input number to string
	nums = str(nums)
	#Delete all zeroes
	nums = nums.replace("0", "")
	#Convert number string into individual numbers
	nums = list(nums)
	#Convert individual numbers into integers
	nums = map(int, nums)


	#Iterate through numbers to calculate product
	k = 0
	product = 1
	while k < len(nums):
		product *= nums[k]
		k += 1
	return product


print digits_multiply(101205004)
#Total should be 40