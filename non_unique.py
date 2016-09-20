#Function that returns only duplicate numbers

def non_unique(*nums):

	dupl_nums = [i for i in nums if nums.count(i) > 1]
	return dupl_nums

print non_unique(1, 2, 3, 4, 2, 6, -1, 0, 8, 3, -1, 3)