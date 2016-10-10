def sort_list(nums):

	for i in range(0, len(nums)):
		for j in range(0, len(nums)):
			if nums[i] < nums[j]:
				temp = nums[i]
				#print 'temp:', nums[i]
				nums[i] = nums[j]
				#print 'i:', nums[i]
				nums[j] = temp
				#print 'j:', nums[j]
	print nums


nums = [1, 5, -7, 8, 3, 22, 4, 0, 99, -34]
sort_list(nums)