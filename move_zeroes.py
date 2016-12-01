def move_zeroes(nums):

	for i in nums:
		if i == 0:
			nums.append(i)
			nums.remove(i)
	print nums


nums = [0, 1, 0, 3, 12]

move_zeroes(nums)